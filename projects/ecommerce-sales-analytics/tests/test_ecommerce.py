import sys
from pathlib import Path
import pytest
import pandas as pd

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.ecommerce_engine import ECommerceAnalyticsEngine

@pytest.fixture
def orders_df():
    data_path = Path(__file__).parent.parent / "data" / "orders.csv"
    assert data_path.exists(), f"Orders file not found at {data_path}"
    return pd.read_csv(data_path)

def test_kpi_computation(orders_df):
    engine = ECommerceAnalyticsEngine(orders_df)
    kpis = engine.compute_kpis()

    assert kpis.total_revenue > 0
    assert kpis.total_orders == 16
    assert kpis.unique_customers == 9
    assert kpis.average_order_value > 0
    assert kpis.top_selling_category in ['Electronics', 'Home & Kitchen', 'Apparel']

def test_monthly_trends(orders_df):
    engine = ECommerceAnalyticsEngine(orders_df)
    trends = engine.get_monthly_trends()

    assert len(trends) == 3 # Jan, Feb, Mar 2026
    assert 'revenue' in trends.columns
    assert 'MoM_Growth_Pct' in trends.columns

def test_category_performance(orders_df):
    engine = ECommerceAnalyticsEngine(orders_df)
    cat_df = engine.get_category_performance()

    assert len(cat_df) >= 4
    assert 'revenue_share_pct' in cat_df.columns
    assert abs(cat_df['revenue_share_pct'].sum() - 100.0) < 0.1

def test_rfm_segmentation(orders_df):
    engine = ECommerceAnalyticsEngine(orders_df)
    rfm = engine.compute_rfm_segmentation(reference_date='2026-04-01')

    assert len(rfm) == 9 # 9 unique customers
    assert 'Segment' in rfm.columns
    assert set(rfm['Segment']).issubset({'Champions', 'Loyal Customers', 'Recent Buyers', 'At Risk / Hibernating'})
