import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import pandas as pd
from src.finance_engine import PersonalFinanceEngine

@pytest.fixture
def sample_transactions():
    return pd.DataFrame({
        'Date': ['2026-01-01', '2026-01-02', '2026-01-15'],
        'Category': ['Salary', 'Groceries', 'Rent'],
        'Description': ['Monthly Pay', 'Food store', 'House rent'],
        'Amount': [50000, 5000, 15000],
        'Type': ['Income', 'Expense', 'Expense']
    })

@pytest.fixture
def sample_budgets():
    return pd.DataFrame({
        'Category': ['Groceries', 'Rent'],
        'Monthly_Budget': [6000, 14000]
    })

def test_kpi_computation(sample_transactions):
    engine = PersonalFinanceEngine(sample_transactions)
    kpis = engine.compute_kpis()

    assert kpis.total_income == 50000
    assert kpis.total_expenses == 20000
    assert kpis.net_savings == 30000
    assert kpis.savings_rate_pct == 60.0
    assert kpis.highest_expense_category == 'Rent'

def test_category_breakdown(sample_transactions):
    engine = PersonalFinanceEngine(sample_transactions)
    cat_df = engine.get_category_breakdown()

    assert len(cat_df) == 2
    assert cat_df.iloc[0]['Category'] == 'Rent'
    assert cat_df.iloc[0]['Total_Amount'] == 15000
    assert cat_df.iloc[0]['Percentage'] == 75.0

def test_budget_variance(sample_transactions, sample_budgets):
    engine = PersonalFinanceEngine(sample_transactions, sample_budgets)
    var_df = engine.get_budget_variance()

    assert len(var_df) == 2
    rent_row = var_df[var_df['Category'] == 'Rent'].iloc[0]
    assert rent_row['Variance'] == -1000  # 14000 - 15000
    assert rent_row['Status'] == 'Over Budget'

def test_missing_columns_validation():
    bad_df = pd.DataFrame({'Wrong': [1, 2]})
    with pytest.raises(ValueError, match="missing required columns"):
        PersonalFinanceEngine(bad_df)
