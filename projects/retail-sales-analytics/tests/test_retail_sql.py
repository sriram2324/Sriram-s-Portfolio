import sys
from pathlib import Path
import os
import pytest

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.retail_analytics import RetailAnalyticsEngine

@pytest.fixture
def db_path():
    db_file = Path(__file__).parent.parent / "data" / "retail.db"
    assert db_file.exists(), f"Database not found at {db_file}"
    return str(db_file)

def test_sales_overview(db_path):
    engine = RetailAnalyticsEngine(db_path)
    overview = engine.get_sales_overview()

    assert overview['total_orders'] == 9
    assert overview['active_customers'] == 6
    assert overview['total_revenue'] > 0
    assert overview['total_profit'] > 0
    assert overview['profit_margin_pct'] > 0

def test_monthly_revenue_trends(db_path):
    engine = RetailAnalyticsEngine(db_path)
    trends = engine.get_monthly_revenue_trends()

    assert len(trends) == 3  # Jan, Feb, Mar 2026
    assert 'month' in trends.columns
    assert 'monthly_revenue' in trends.columns
    assert trends['monthly_revenue'].sum() > 0

def test_category_performance(db_path):
    engine = RetailAnalyticsEngine(db_path)
    cat_df = engine.get_category_performance()

    assert len(cat_df) >= 3
    assert 'Furniture' in cat_df['category'].values
    assert 'Technology' in cat_df['category'].values

def test_customer_patterns(db_path):
    engine = RetailAnalyticsEngine(db_path)
    cust_df = engine.get_customer_purchasing_patterns()

    assert len(cust_df) == 6
    assert cust_df.iloc[0]['total_spend'] >= cust_df.iloc[-1]['total_spend']
