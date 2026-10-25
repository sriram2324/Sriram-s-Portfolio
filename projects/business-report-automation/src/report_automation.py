"""Business Performance Reporting Automation Engine.

Automates ingestion of multi-department commercial metrics, computes key financial KPIs,
evaluates target attainment and operating margins, and exports repeatable executive reports.
"""

from typing import Dict, Any, List
import pandas as pd
import numpy as np

class BusinessReportEngine:
    REQUIRED_COLUMNS = {
        'Month', 'Department', 'Target_Revenue', 'Actual_Revenue', 'Operational_Cost', 'Headcount'
    }

    def __init__(self, data_path_or_df):
        if isinstance(data_path_or_df, str):
            self.df = pd.read_csv(data_path_or_df)
        elif isinstance(data_path_or_df, pd.DataFrame):
            self.df = data_path_or_df.copy()
        else:
            raise TypeError("Expected file path or pandas DataFrame")

        self._validate_schema()
        self._calculate_derived_fields()

    def _validate_schema(self):
        missing = self.REQUIRED_COLUMNS - set(self.df.columns)
        if missing:
            raise ValueError(f"Missing required columns in business dataset: {missing}")

    def _calculate_derived_fields(self):
        self.df['Target_Revenue'] = pd.to_numeric(self.df['Target_Revenue'], errors='coerce')
        self.df['Actual_Revenue'] = pd.to_numeric(self.df['Actual_Revenue'], errors='coerce')
        self.df['Operational_Cost'] = pd.to_numeric(self.df['Operational_Cost'], errors='coerce')
        self.df['Headcount'] = pd.to_numeric(self.df['Headcount'], errors='coerce')

        # Derived business KPIs
        self.df['Gross_Profit'] = self.df['Actual_Revenue'] - self.df['Operational_Cost']
        self.df['Operating_Margin_Pct'] = (self.df['Gross_Profit'] / self.df['Actual_Revenue'] * 100).round(2)
        self.df['Target_Attainment_Pct'] = (self.df['Actual_Revenue'] / self.df['Target_Revenue'] * 100).round(2)
        self.df['Revenue_Per_Employee'] = (self.df['Actual_Revenue'] / self.df['Headcount']).round(2)

    def get_company_overview(self) -> Dict[str, Any]:
        tot_target = self.df['Target_Revenue'].sum()
        tot_actual = self.df['Actual_Revenue'].sum()
        tot_cost = self.df['Operational_Cost'].sum()
        tot_profit = tot_actual - tot_cost
        avg_margin = (tot_profit / tot_actual * 100).round(2) if tot_actual > 0 else 0.0
        attainment = (tot_actual / tot_target * 100).round(2) if tot_target > 0 else 0.0

        return {
            'total_target_revenue': float(tot_target),
            'total_actual_revenue': float(tot_actual),
            'total_operational_cost': float(tot_cost),
            'total_gross_profit': float(tot_profit),
            'overall_margin_pct': float(avg_margin),
            'target_attainment_pct': float(attainment),
            'status': 'Ahead of Target' if attainment >= 100.0 else 'Behind Target'
        }

    def get_department_performance(self) -> pd.DataFrame:
        dept = self.df.groupby('Department').agg(
            Target_Revenue=('Target_Revenue', 'sum'),
            Actual_Revenue=('Actual_Revenue', 'sum'),
            Operational_Cost=('Operational_Cost', 'sum'),
            Avg_Headcount=('Headcount', 'mean')
        ).reset_index()

        dept['Gross_Profit'] = dept['Actual_Revenue'] - dept['Operational_Cost']
        dept['Operating_Margin_Pct'] = (dept['Gross_Profit'] / dept['Actual_Revenue'] * 100).round(2)
        dept['Target_Attainment_Pct'] = (dept['Actual_Revenue'] / dept['Target_Revenue'] * 100).round(2)
        return dept.sort_values(by='Actual_Revenue', ascending=False)

    def generate_executive_markdown_report(self) -> str:
        overview = self.get_company_overview()
        dept = self.get_department_performance()

        report_lines = [
            "# Executive Business Performance & KPI Report",
            f"**Status**: {overview['status']} ({overview['target_attainment_pct']}% attainment)",
            "",
            "## 1. Key Performance Indicators",
            f"- **Target Revenue**: ₹{overview['total_target_revenue']:,.2f}",
            f"- **Actual Revenue**: ₹{overview['total_actual_revenue']:,.2f}",
            f"- **Operating Cost**: ₹{overview['total_operational_cost']:,.2f}",
            f"- **Gross Profit**: ₹{overview['total_gross_profit']:,.2f}",
            f"- **Overall Operating Margin**: {overview['overall_margin_pct']}%",
            "",
            "## 2. Department Breakdown",
        ]

        for _, row in dept.iterrows():
            report_lines.append(
                f"- **{row['Department']}**: ₹{row['Actual_Revenue']:,.0f} Actual "
                f"({row['Target_Attainment_Pct']}% Attainment, {row['Operating_Margin_Pct']}% Margin)"
            )

        return "\n".join(report_lines)
