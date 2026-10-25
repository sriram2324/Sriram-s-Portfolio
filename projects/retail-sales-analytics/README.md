# Retail Sales Analytics with SQL

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57.svg)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)

A commercial retail intelligence and relational analytics pipeline using SQL and Python. It analyzes order transactions, revenue growth trends, product performance hierarchies, and customer purchasing patterns.

---

## 🌟 Key Features

1. **Relational Database Design**:
   - 4 normalized relational tables (`customers`, `products`, `orders`, `order_items`) with foreign key constraints.
2. **Advanced SQL Query Engine**:
   - Multi-table joins and date extractions (`strftime('%Y-%m', o.order_date)`).
   - Aggregations calculating revenue, gross margins, and item order counts.
3. **Customer Purchasing Patterns**:
   - Customer segmentation across `Consumer`, `Corporate`, and `Home Office`.
   - Identification of repeat buyers and basket sizes.
4. **Automated Testing**:
   - Pytest test suite asserting query accuracy, financial calculations, and data consistency.

---

## 🛠️ Technology Stack

- **Relational Storage**: SQLite
- **Language**: Python 3.10+
- **Data Manipulation**: `pandas`
- **Visualization Ready**: `plotly`
- **Testing**: `pytest`

---

## 🚀 Setup & Execution

1. **Seed the Relational Database**:
   ```bash
   python data/seed_data.py
   ```

2. **Run the Test Suite**:
   ```bash
   python -m pytest tests/
   ```
