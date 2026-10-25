"""Personal Finance & Expense Intelligence Dashboard - Streamlit Application."""

import os
import pandas as pd
import plotly.express as px
import streamlit as st
from src.finance_engine import PersonalFinanceEngine

st.set_page_config(page_title="Personal Finance Intelligence", page_icon="💰", layout="wide")

st.title("💰 Personal Finance & Expense Intelligence Dashboard")
st.markdown("Track income, analyze categorical expenses, monitor budget variances, and evaluate savings velocity.")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
trans_path = os.path.join(DATA_DIR, "transactions.csv")
budgets_path = os.path.join(DATA_DIR, "budgets.csv")

# File uploader or default dataset
uploaded_file = st.sidebar.file_uploader("Upload Transactions CSV", type=["csv"])
if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
elif os.path.exists(trans_path):
    df_raw = pd.read_csv(trans_path)
else:
    df_raw = pd.DataFrame()

df_budgets = pd.read_csv(budgets_path) if os.path.exists(budgets_path) else None

if not df_raw.empty:
    engine = PersonalFinanceEngine(df_raw, df_budgets)
    kpis = engine.compute_kpis()

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Inflow", f"₹{kpis.total_income:,.0f}")
    m2.metric("Total Expenses", f"₹{kpis.total_expenses:,.0f}")
    m3.metric("Net Savings", f"₹{kpis.net_savings:,.0f}", delta=f"{kpis.savings_rate_pct}% Rate")
    m4.metric("Avg Monthly Expense", f"₹{kpis.avg_monthly_expense:,.0f}")

    # Tabs
    t1, t2, t3 = st.tabs(["Expense Breakdown", "Monthly Trends", "Budget Variance"])

    with t1:
        c1, c2 = st.columns([1, 1])
        cat_df = engine.get_category_breakdown()
        fig_pie = px.pie(cat_df, names="Category", values="Total_Amount", title="Expenses by Category", hole=0.4)
        c1.plotly_chart(fig_pie, use_container_width=True)
        c2.dataframe(cat_df, use_container_width=True)

    with t2:
        trend_df = engine.get_monthly_trends()
        fig_trend = px.bar(trend_df, x="Month", y=["Income", "Expense"], barmode="group", title="Monthly Inflows vs Outflows")
        st.plotly_chart(fig_trend, use_container_width=True)

    with t3:
        var_df = engine.get_budget_variance()
        if not var_df.empty:
            st.dataframe(var_df.style.map(lambda v: "color: red;" if v == "Over Budget" else "color: green;", subset=["Status"]), use_container_width=True)

    # Downloadable CSV report
    csv_report = cat_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Category Expense Report", data=csv_report, file_name="expense_category_report.csv", mime="text/csv")
else:
    st.info("Please upload a transaction CSV file with Date, Category, Description, Amount, and Type columns.")
