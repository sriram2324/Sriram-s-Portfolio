"""Personal Finance & Expense Intelligence Engine.

Provides core analytical processing, transaction validation, budget tracking,
financial KPI calculation, and report export logic.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import pandas as pd
import numpy as np


@dataclass
class FinancialKPIs:
    total_income: float
    total_expenses: float
    net_savings: float
    savings_rate_pct: float
    avg_monthly_expense: float
    highest_expense_category: str


class PersonalFinanceEngine:
    REQUIRED_TRANSACTION_COLS = {'Date', 'Category', 'Description', 'Amount', 'Type'}
    REQUIRED_BUDGET_COLS = {'Category', 'Monthly_Budget'}

    def __init__(self, transactions_df: pd.DataFrame, budgets_df: Optional[pd.DataFrame] = None):
        self.transactions = self._clean_and_validate_transactions(transactions_df)
        self.budgets = self._validate_budgets(budgets_df) if budgets_df is not None else pd.DataFrame(columns=['Category', 'Monthly_Budget'])

    def _clean_and_validate_transactions(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = self.REQUIRED_TRANSACTION_COLS - set(df.columns)
        if missing:
            raise ValueError(f"Transactions dataset missing required columns: {missing}")

        data = df.copy()
        data['Date'] = pd.to_datetime(data['Date'])
        data['Amount'] = pd.to_numeric(data['Amount'], errors='coerce')
        data = data.dropna(subset=['Date', 'Amount'])
        data = data[data['Amount'] > 0]
        data['Type'] = data['Type'].astype(str).str.strip().str.capitalize()
        data['Category'] = data['Category'].astype(str).str.strip()
        data['Month'] = data['Date'].dt.to_period('M').astype(str)
        return data

    def _validate_budgets(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = self.REQUIRED_BUDGET_COLS - set(df.columns)
        if missing:
            raise ValueError(f"Budgets dataset missing required columns: {missing}")
        b = df.copy()
        b['Monthly_Budget'] = pd.to_numeric(b['Monthly_Budget'], errors='coerce').fillna(0)
        return b

    def compute_kpis(self) -> FinancialKPIs:
        income = self.transactions[self.transactions['Type'] == 'Income']['Amount'].sum()
        expenses = self.transactions[self.transactions['Type'] == 'Expense']['Amount'].sum()
        net_savings = income - expenses
        savings_rate = (net_savings / income * 100) if income > 0 else 0.0

        months_count = max(1, self.transactions['Month'].nunique())
        avg_monthly = expenses / months_count

        exp_df = self.transactions[self.transactions['Type'] == 'Expense']
        if not exp_df.empty:
            cat_totals = exp_df.groupby('Category')['Amount'].sum()
            top_cat = cat_totals.idxmax()
        else:
            top_cat = "None"

        return FinancialKPIs(
            total_income=float(income),
            total_expenses=float(expenses),
            net_savings=float(net_savings),
            savings_rate_pct=round(float(savings_rate), 2),
            avg_monthly_expense=round(float(avg_monthly), 2),
            highest_expense_category=str(top_cat)
        )

    def get_category_breakdown(self) -> pd.DataFrame:
        exp_df = self.transactions[self.transactions['Type'] == 'Expense']
        if exp_df.empty:
            return pd.DataFrame(columns=['Category', 'Total_Amount', 'Percentage'])
        totals = exp_df.groupby('Category')['Amount'].sum().reset_index()
        totals.columns = ['Category', 'Total_Amount']
        sum_exp = totals['Total_Amount'].sum()
        totals['Percentage'] = (totals['Total_Amount'] / sum_exp * 100).round(2)
        return totals.sort_values(by='Total_Amount', ascending=False)

    def get_monthly_trends(self) -> pd.DataFrame:
        pvt = self.transactions.pivot_table(
            index='Month',
            columns='Type',
            values='Amount',
            aggfunc='sum',
            fill_value=0
        ).reset_index()

        if 'Income' not in pvt.columns:
            pvt['Income'] = 0.0
        if 'Expense' not in pvt.columns:
            pvt['Expense'] = 0.0

        pvt['Net_Savings'] = pvt['Income'] - pvt['Expense']
        return pvt.sort_values(by='Month')

    def get_budget_variance(self) -> pd.DataFrame:
        if self.budgets.empty:
            return pd.DataFrame()

        exp_df = self.transactions[self.transactions['Type'] == 'Expense']
        months = max(1, self.transactions['Month'].nunique())
        actuals = exp_df.groupby('Category')['Amount'].sum() / months
        actuals = actuals.reset_index().rename(columns={'Amount': 'Avg_Monthly_Actual'})

        merged = pd.merge(self.budgets, actuals, on='Category', how='left').fillna(0)
        merged['Variance'] = merged['Monthly_Budget'] - merged['Avg_Monthly_Actual']
        merged['Status'] = np.where(merged['Variance'] >= 0, 'Under Budget', 'Over Budget')
        return merged
