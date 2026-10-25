# Customer Churn Prediction Machine Learning Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Pipeline-F7931E.svg)](https://scikit-learn.org/)
[![Tests](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)

A reproducible machine learning classification pipeline designed to identify subscription customer churn risk. Built with strict data-hygiene standards guaranteeing zero data leakage, modular preprocessing, multi-model benchmarking, and feature importance explainability.

---

## 🌟 Key Features

1. **Zero Data Leakage Pipeline**:
   - `ColumnTransformer` with `StandardScaler` and `OneHotEncoder` fitted strictly on training data and applied to held-out test splits.
2. **Multi-Model Benchmarking**:
   - Baseline: `LogisticRegression` with regularized solver.
   - Classification: `RandomForestClassifier` with ensemble tree aggregation.
3. **Comprehensive Evaluation Metrics**:
   - Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and ROC-AUC score.
4. **Explainable Feature Importance**:
   - Tree Gini-importance ranking identifying key behavioral drivers of churn (e.g., Tenure, Contract duration, Monthly Charges).
5. **Automated Unit Testing**:
   - Pytest suite verifying data splits, preprocessing isolation, and evaluation validity.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Machine Learning**: `scikit-learn`
- **Visualization Ready**: `matplotlib`, `seaborn`
- **Testing**: `pytest`

---

## 🚀 Setup & Execution

1. **Generate or Verify Dataset**:
   ```bash
   python data/generate_data.py
   ```

2. **Run Automated Test Suite**:
   ```bash
   python -m pytest tests/
   ```
