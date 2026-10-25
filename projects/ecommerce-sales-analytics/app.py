"""E-Commerce Sales Analytics & Customer Segmentation Dashboard."""

import os
import pandas as pd
import plotly.express as px
import streamlit as st
from src.ecommerce_engine import ECommerceAnalyticsEngine

st.set_page_config(page_title="E-Commerce Sales Analytics", page_icon="🛒", layout="wide")

st.title("🛒 E-Commerce Sales Analytics & KPI Intelligence")
st.markdown("Analyze monthly and seasonal trends, catalog performance, and RFM customer segmentation.")

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "orders.csv")

if os.path.exists(DATA_PATH):
    df_raw = pd.read_csv(DATA_PATH)
    engine = ECommerceAnalyticsEngine(df_raw)
    kpis = engine.compute_kpis()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gross Revenue", f"₹{kpis.total_revenue:,.0f}")
    c2.metric("Total Orders", f"{kpis.total_orders:,}")
    c3.metric("Average Order Value (AOV)", f"₹{kpis.average_order_value:,.0f}")
    c4.metric("Active Customers", f"{kpis.unique_customers}")

    t1, t2, t3 = st.tabs(["Monthly & Seasonal Trends", "Category Performance", "RFM Customer Segmentation"])

    with t1:
        trends = engine.get_monthly_trends()
        fig_trend = px.line(trends, x="Month", y="revenue", markers=True, title="Monthly Revenue Trajectory (₹)")
        st.plotly_chart(fig_trend, use_container_width=True)
        st.dataframe(trends, use_container_width=True)

    with t2:
        cat_df = engine.get_category_performance()
        fig_cat = px.bar(cat_df, x="Category", y="revenue", color="Category", title="Revenue Contribution by Product Category")
        st.plotly_chart(fig_cat, use_container_width=True)

    with t3:
        rfm_df = engine.compute_rfm_segmentation()
        fig_rfm = px.pie(rfm_df, names="Segment", title="Customer Cohort Distribution (RFM)")
        st.plotly_chart(fig_rfm, use_container_width=True)
        st.dataframe(rfm_df, use_container_width=True)

    # Downloadable summary
    csv_data = cat_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Category Performance Report", data=csv_data, file_name="ecommerce_category_report.csv", mime="text/csv")
else:
    st.error("Dataset not found at data/orders.csv")
