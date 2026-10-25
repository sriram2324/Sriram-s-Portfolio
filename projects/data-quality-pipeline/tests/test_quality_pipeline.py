import sys
from pathlib import Path
import pytest
import pandas as pd

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.quality_pipeline import DataQualityPipeline

@pytest.fixture
def raw_df():
    data_path = Path(__file__).parent.parent / "data" / "raw_dirty_users.csv"
    assert data_path.exists(), f"Raw dirty data file not found at {data_path}"
    return pd.read_csv(data_path)

def test_pipeline_execution(raw_df):
    pipeline = DataQualityPipeline(raw_df)
    metrics = pipeline.run_pipeline()

    assert metrics.total_raw_rows == 10
    assert metrics.duplicates_removed == 1 # USR_102 duplicated
    assert metrics.final_clean_rows == 9
    assert metrics.missing_cells_repaired >= 2
    assert metrics.outliers_detected >= 1
    assert metrics.data_quality_score_pct > 80.0

def test_schema_validation_failure():
    bad_df = pd.DataFrame({'invalid_col': [1, 2]})
    pipeline = DataQualityPipeline(bad_df)
    with pytest.raises(ValueError, match="Schema Validation Failed"):
        pipeline.validate_schema()

def test_report_generation(raw_df):
    pipeline = DataQualityPipeline(raw_df)
    report = pipeline.generate_markdown_report()

    assert "# Automated Data Quality & Integrity Report" in report
    assert "Overall Data Quality Score" in report
    assert len(pipeline.audit_log) > 0
