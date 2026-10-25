"""Tests for isolated cleanup behavior and session reset safety."""

from pathlib import Path
import pytest

from news_sentiment.cleanup import clean_temp_directory, reset_streamlit_session
from news_sentiment.config import PROJECT_ROOT, DATA_DIR, MODELS_DIR, REPORTS_DIR


def test_test_temp_files_removed_after_test(tmp_path: Path):
    """Temporary test files created inside dedicated sandbox must be purged."""
    sandbox = tmp_path / ".temp_test_sandbox"
    sandbox.mkdir(parents=True, exist_ok=True)
    temp_file = sandbox / "temp_fixture.csv"
    temp_file.write_text("text,label\nHeadline,positive\n")

    assert temp_file.exists()

    result = clean_temp_directory(temp_dir=sandbox, allowed_root=tmp_path)
    assert result["success"] is True
    assert not temp_file.exists()


def test_cleanup_protects_production_data_and_models():
    """Cleanup must strictly refuse to delete protected directories like data, models, reports."""
    for protected_dir in [DATA_DIR, MODELS_DIR, REPORTS_DIR, PROJECT_ROOT]:
        result = clean_temp_directory(temp_dir=protected_dir, allowed_root=PROJECT_ROOT)
        assert result["success"] is False
        assert "protected" in result["error"].lower() or "not an isolated inner subpath" in result["error"].lower()


def test_reset_action_clears_stale_session_keys():
    """Reset session helper must remove transient UI state while avoiding KeyError or iteration bugs."""
    mock_session_state = {
        "single_text_input": "Company reports record profit",
        "single_prediction_result": {"label": "positive"},
        "uploaded_csv_data": "raw data",
        "batch_predictions_df": "df",
        "filter_sentiment": "positive",
        "temp_random_key": 12345,
        "persistent_theme": "dark",
        "model_version": "1.0.0"
    }

    cleared = reset_streamlit_session(mock_session_state)

    assert "single_text_input" in cleared
    assert "single_prediction_result" in cleared
    assert "batch_predictions_df" in cleared
    assert "filter_sentiment" in cleared
    assert "temp_random_key" in cleared

    assert "single_text_input" not in mock_session_state
    assert "batch_predictions_df" not in mock_session_state
    assert "persistent_theme" in mock_session_state
    assert mock_session_state["persistent_theme"] == "dark"
    assert mock_session_state["model_version"] == "1.0.0"
