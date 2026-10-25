import sys
from pathlib import Path
import pytest
import pandas as pd

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.report_automation import BusinessReportEngine

@pytest.fixture
def performance_csv():
    data_path = Path(__file__).parent.parent / "data" / "business_performance.csv"
    assert data_path.exists(), f"File not found: {data_path}"
    return str(data_path)

def test_company_overview(performance_csv):
    engine = BusinessReportEngine(performance_csv)
    ov = engine.get_company_overview()

    assert ov['total_actual_revenue'] > ov['total_operational_cost']
    assert ov['total_gross_profit'] > 0
    assert ov['overall_margin_pct'] > 0
    assert ov['target_attainment_pct'] > 95.0
    assert ov['status'] == 'Ahead of Target'

def test_department_performance(performance_csv):
    engine = BusinessReportEngine(performance_csv)
    dept_df = engine.get_department_performance()

    assert len(dept_df) == 3
    assert 'Enterprise Sales' in dept_df['Department'].values
    assert dept_df.iloc[0]['Actual_Revenue'] >= dept_df.iloc[-1]['Actual_Revenue']

def test_executive_markdown_report(performance_csv):
    engine = BusinessReportEngine(performance_csv)
    report = engine.generate_executive_markdown_report()

    assert "# Executive Business Performance & KPI Report" in report
    assert "Target Revenue" in report
    assert "Enterprise Sales" in report
