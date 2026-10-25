"""E-Commerce Sales Analytics Engine.

Provides revenue calculations, seasonal trend analysis, product & category performance metrics,
and Recency-Frequency-Monetary (RFM) customer segmentation.
"""

from dataclasses import dataclass
from typing import Dict, Any
import pandas as pd
import numpy as np

@dataclass
class ECommerceKPIs:
    total_revenue: float
    total_orders: int
    total_units_sold: int
    average_order_value: float
    unique_customers: int
    top_selling_category: str

class ECommerceAnalyticsEngine:
    REQUIRED_COLUMNS = {
        'Order_ID', 'Date', 'Customer_ID', 'Category',
        'Product_Name', 'Quantity', 'Unit_Price', 'Total_Revenue'
    }

    def __init__(self, df: pd.DataFrame):
        self.df = self._validate_and_clean(df)

    def _validate_and_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = self.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns in e-commerce dataset: {missing}")

        data = df.copy()
        data['Date'] = pd.to_datetime(data['Date'])
        data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce').fillna(0).astype(int)
        data['Unit_Price'] = pd.to_numeric(data['Unit_Price'], errors='coerce').fillna(0.0)
        data['Total_Revenue'] = pd.to_numeric(data['Total_Revenue'], errors='coerce').fillna(0.0)
        data['Month'] = data['Date'].dt.to_period('M').astype(str)
        return data

    def compute_kpis(self) -> ECommerceKPIs:
        total_rev = self.df['Total_Revenue'].sum()
        total_ord = self.df['Order_ID'].nunique()
        total_qty = self.df['Quantity'].sum()
        aov = (total_rev / total_ord) if total_ord > 0 else 0.0
        uniq_cust = self.df['Customer_ID'].nunique()

        top_cat = self.df.groupby('Category')['Total_Revenue'].sum().idxmax() if not self.df.empty else "N/A"

        return ECommerceKPIs(
            total_revenue=round(float(total_rev), 2),
            total_orders=int(total_ord),
            total_units_sold=int(total_qty),
            average_order_value=round(float(aov), 2),
            unique_customers=int(uniq_cust),
            top_selling_category=str(top_cat)
        )

    def get_monthly_trends(self) -> pd.DataFrame:
        trends = self.df.groupby('Month').agg(
            revenue=('Total_Revenue', 'sum'),
            orders=('Order_ID', 'nunique'),
            units=('Quantity', 'sum')
        ).reset_index()
        trends['MoM_Growth_Pct'] = trends['revenue'].pct_change().fillna(0).round(4) * 100
        return trends.sort_values(by='Month')

    def get_category_performance(self) -> pd.DataFrame:
        cat_df = self.df.groupby('Category').agg(
            revenue=('Total_Revenue', 'sum'),
            orders=('Order_ID', 'nunique'),
            units_sold=('Quantity', 'sum'),
            avg_price=('Unit_Price', 'mean')
        ).reset_index()
        tot_rev = cat_df['revenue'].sum()
        cat_df['revenue_share_pct'] = (cat_df['revenue'] / tot_rev * 100).round(2) if tot_rev > 0 else 0.0
        return cat_df.sort_values(by='revenue', ascending=False)

    def compute_rfm_segmentation(self, reference_date: str = '2026-04-01') -> pd.DataFrame:
        ref_dt = pd.to_datetime(reference_date)
        rfm = self.df.groupby('Customer_ID').agg(
            Recency_Days=('Date', lambda x: (ref_dt - x.max()).days),
            Frequency=('Order_ID', 'nunique'),
            Monetary=('Total_Revenue', 'sum')
        ).reset_index()

        # Segment assignment based on frequency & monetary thresholds
        def assign_segment(row):
            if row['Frequency'] >= 3 or row['Monetary'] >= 10000:
                return 'Champions'
            elif row['Frequency'] == 2 and row['Recency_Days'] <= 45:
                return 'Loyal Customers'
            elif row['Recency_Days'] <= 30:
                return 'Recent Buyers'
            else:
                return 'At Risk / Hibernating'

        rfm['Segment'] = rfm.apply(assign_segment, axis=1)
        return rfm.sort_values(by='Monetary', ascending=False)
