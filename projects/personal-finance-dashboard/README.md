# Personal Finance & Expense Intelligence Dashboard

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Tests](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)

An end-to-end personal finance analytics and budgeting application. It automates financial transaction validation, audits monthly cash flows, monitors category budget variances, and renders interactive Plotly visualizations in a modern Streamlit interface.

---

## 🌟 Key Features

1. **Transaction Ingestion & Cleaning**:
   - Enforces strict schema validation (`Date`, `Category`, `Description`, `Amount`, `Type`).
   - Cleans date formats and discards invalid non-positive transactions safely.
2. **Key Financial KPIs**:
   - Total Inflow, Total Outflow, Net Savings, and Savings Rate (%) tracking.
   - Automatic identification of top spending categories.
3. **Budget vs. Actual Variance Engine**:
   - Month-by-month category budget tracking.
   - Highlights over-budget and under-budget spending patterns.
4. **Interactive Visual Dashboard**:
   - Plotly category breakdown donut chart.
   - Grouped bar chart comparing monthly income vs. expenses.
   - CSV export for executive summaries.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Visualization**: `plotly`
- **Application Framework**: `streamlit`
- **Automated Testing**: `pytest`

---

## 🚀 Quick Start Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Automated Tests**:
   ```bash
   pytest tests/
   ```

3. **Launch the Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

## 📊 Dataset Specification

The project includes realistic synthetic data in `data/transactions.csv` and category targets in `data/budgets.csv`.
- License: Creative Commons Zero v1.0 Universal (`CC0 1.0`).
- No private financial credentials or account numbers are collected or stored.
