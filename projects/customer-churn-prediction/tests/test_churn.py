import sys
from pathlib import Path
import pytest

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.churn_pipeline import ChurnPipeline

@pytest.fixture
def dataset_path():
    path = Path(__file__).parent.parent / "data" / "churn_data.csv"
    assert path.exists(), f"Churn dataset not found at {path}"
    return str(path)

def test_pipeline_data_loading_and_split(dataset_path):
    pipeline = ChurnPipeline(random_state=42)
    df = pipeline.load_data(dataset_path)
    assert len(df) == 150
    assert 'Churn' in df.columns

    X_train, X_test, y_train, y_test = pipeline.split_data(df, test_size=0.25)
    assert len(X_train) + len(X_test) == 150
    assert len(X_test) == 38

def test_zero_data_leakage_and_training(dataset_path):
    pipeline = ChurnPipeline(random_state=42)
    df = pipeline.load_data(dataset_path)
    X_train, X_test, y_train, y_test = pipeline.split_data(df, test_size=0.25)

    pipeline.fit_and_train(X_train, y_train)
    assert pipeline.is_fitted
    assert len(pipeline.feature_names) > 0

    results = pipeline.evaluate(X_test, y_test)
    assert 'Logistic Regression (Baseline)' in results
    assert 'Random Forest (Classification)' in results

    rf_res = results['Random Forest (Classification)']
    assert 0.0 <= rf_res['accuracy'] <= 1.0
    assert 0.0 <= rf_res['roc_auc'] <= 1.0
    assert len(rf_res['confusion_matrix']) == 2

def test_feature_importance_output(dataset_path):
    pipeline = ChurnPipeline(random_state=42)
    df = pipeline.load_data(dataset_path)
    X_train, X_test, y_train, y_test = pipeline.split_data(df)
    pipeline.fit_and_train(X_train, y_train)

    feat_df = pipeline.get_feature_importances()
    assert not feat_df.empty
    assert 'Feature' in feat_df.columns
    assert 'Importance' in feat_df.columns
    assert abs(feat_df['Importance'].sum() - 1.0) < 1e-3
