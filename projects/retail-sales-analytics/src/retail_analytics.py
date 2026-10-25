"""Retail Sales Analytics Engine with SQL."""

import sqlite3
import pandas as pd
from typing import Dict, Any

class RetailAnalyticsEngine:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def get_sales_overview(self) -> Dict[str, Any]:
        query = """
        SELECT
            COUNT(DISTINCT o.order_id) as total_orders,
            COUNT(DISTINCT o.customer_id) as active_customers,
            ROUND(SUM(oi.quantity * oi.unit_sale_price), 2) as total_revenue,
            ROUND(SUM(oi.quantity * (oi.unit_sale_price - p.cost_price)), 2) as total_profit
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        WHERE o.status = 'Delivered';
        """
        with self._get_connection() as conn:
            df = pd.read_sql_query(query, conn)
            res = df.iloc[0].to_dict()
            res['profit_margin_pct'] = round((res['total_profit'] / res['total_revenue'] * 100), 2) if res['total_revenue'] > 0 else 0
            return res

    def get_monthly_revenue_trends(self) -> pd.DataFrame:
        query = """
        SELECT
            strftime('%Y-%m', o.order_date) as month,
            COUNT(DISTINCT o.order_id) as order_count,
            ROUND(SUM(oi.quantity * oi.unit_sale_price), 2) as monthly_revenue,
            ROUND(SUM(oi.quantity * (oi.unit_sale_price - p.cost_price)), 2) as monthly_profit
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        WHERE o.status = 'Delivered'
        GROUP BY strftime('%Y-%m', o.order_date)
        ORDER BY month ASC;
        """
        with self._get_connection() as conn:
            return pd.read_sql_query(query, conn)

    def get_category_performance(self) -> pd.DataFrame:
        query = """
        SELECT
            p.category,
            COUNT(DISTINCT oi.order_id) as orders_included,
            SUM(oi.quantity) as total_units_sold,
            ROUND(SUM(oi.quantity * oi.unit_sale_price), 2) as revenue,
            ROUND(SUM(oi.quantity * (oi.unit_sale_price - p.cost_price)), 2) as profit
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN orders o ON oi.order_id = o.order_id
        WHERE o.status = 'Delivered'
        GROUP BY p.category
        ORDER BY revenue DESC;
        """
        with self._get_connection() as conn:
            return pd.read_sql_query(query, conn)

    def get_customer_purchasing_patterns(self) -> pd.DataFrame:
        query = """
        SELECT
            c.customer_id,
            c.name,
            c.segment,
            c.city,
            COUNT(DISTINCT o.order_id) as order_count,
            ROUND(SUM(oi.quantity * oi.unit_sale_price), 2) as total_spend,
            ROUND(AVG(oi.quantity * oi.unit_sale_price), 2) as avg_item_spend
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status = 'Delivered'
        GROUP BY c.customer_id, c.name, c.segment, c.city
        ORDER BY total_spend DESC;
        """
        with self._get_connection() as conn:
            return pd.read_sql_query(query, conn)
