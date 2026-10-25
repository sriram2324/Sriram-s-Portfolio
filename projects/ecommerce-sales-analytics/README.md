# E-Commerce Sales Analytics & Customer Segmentation

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)](https://streamlit.io/)
[![Tests](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)

An enterprise-ready e-commerce analytics pipeline and executive Streamlit dashboard. Delivers revenue analysis, monthly trajectory modeling, category performance rankings, and Recency-Frequency-Monetary (RFM) customer segmentation.

---

## 🌟 Key Features

1. **Executive Financial KPIs**:
   - Real-time tracking of Gross Revenue, Order Volume, Units Sold, and Average Order Value (AOV).
2. **Monthly & Seasonal Revenue Modeling**:
   - Month-over-Month (MoM) growth trajectory and seasonal transaction velocity.
3. **Category Contribution Hierarchy**:
   - Product category share of revenue with interactive Plotly visual breakdown.
4. **RFM Customer Segmentation Engine**:
   - Behavioral customer segmentation into `Champions`, `Loyal Customers`, `Recent Buyers`, and `At Risk`.
5. **Report Export**:
   - One-click CSV download for executive reporting.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Visualization**: `plotly`
- **App Framework**: `streamlit`
- **Testing**: `pytest`

---

## 🚀 Setup & Execution

1. **Run Automated Tests**:
   ```bash
   python -m pytest tests/
   ```

2. **Launch Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```
