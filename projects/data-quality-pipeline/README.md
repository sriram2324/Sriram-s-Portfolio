# Data Cleaning & Quality Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Testing](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)
[![SQL & Data](https://img.shields.io/badge/Pandas-Quality-teal.svg)](https://pandas.pydata.org/)

An automated, reusable data cleaning, schema validation, and data quality scoring pipeline. It audits raw unstructured data, repairs missing values with statistical imputers, removes duplicate keys, clips statistical outliers using IQR, and generates audit reports.

---

## 🌟 Key Features

1. **Schema & Data Type Validation**:
   - Asserts column presence, correct data types, and temporal formats.
2. **Deterministic Missing-Value Imputation**:
   - Imputes numeric columns with robust median values and categorical fields with standardized fallback markers.
3. **Duplicate Detection & Deduplication**:
   - Detects exact matches on natural or composite keys (`user_id`, `email`) while keeping audit trails.
4. **Statistical Outlier Detection (IQR)**:
   - Uses the $1.5 \times \text{IQR}$ rule to detect and cap extreme domain values.
5. **Quality Scoring & Markdown Report Generation**:
   - Calculates a normalized Data Quality Score (%) and compiles an executive markdown summary.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Testing**: `pytest`

---

## 🚀 Setup & Execution

```bash
# Run automated tests
python -m pytest tests/
```
