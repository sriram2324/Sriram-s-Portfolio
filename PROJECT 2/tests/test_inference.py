"""Tests for single headline inference and model reloading."""

from pathlib import Path
import joblib
import pytest

from news_sentiment.config import ALLOWED_LABELS
from news_sentiment.inference import predict_single
from news_sentiment.model import load_pipeline


def test_valid_headline_prediction_allowed_class(trained_test_pipeline):
    """Predicting a valid headline must return one of the allowed classes."""
    res = predict_single(
        "Quarterly net profit expanded beating market consensus",
        trained_test_pipeline
    )
    assert res["label"] in ALLOWED_LABELS
    assert isinstance(res["confidence"], float)
    assert 0.0 <= res["confidence"] <= 1.0
    assert "positive" in res["probabilities"]
    assert "negative" in res["probabilities"]
    assert "neutral" in res["probabilities"]


def test_blank_input_raises_in_inference(trained_test_pipeline):
    """Calling predict_single with empty or whitespace string must raise ValueError."""
    with pytest.raises(ValueError, match="blank or only whitespace"):
        predict_single("    ", trained_test_pipeline)


def test_model_artifact_missing_handled(tmp_path: Path):
    """Missing model artifact must raise FileNotFoundError with actionable instructions."""
    non_existent = tmp_path / "missing_model.joblib"
    with pytest.raises(FileNotFoundError, match="Model artifact not found"):
        load_pipeline(non_existent)


def test_saved_model_reload_deterministic(trained_test_pipeline, tmp_path: Path):
    """Saved model reload must produce identical predictions and confidence scores."""
    model_path = tmp_path / "test_pipeline.joblib"
    joblib.dump(trained_test_pipeline, model_path)

    reloaded_model = load_pipeline(model_path)
    test_headline = "Central bank leaves interest rates unchanged at policy summit"

    pred_original = predict_single(test_headline, trained_test_pipeline)
    pred_reloaded = predict_single(test_headline, reloaded_model)

    assert pred_original["label"] == pred_reloaded["label"]
    assert pred_original["confidence"] == pred_reloaded["confidence"]
    assert pred_original["probabilities"] == pred_reloaded["probabilities"]


def test_invalid_pipeline_artifact_rejected(tmp_path: Path):
    """Loading a non-pipeline joblib object must fail with a descriptive ValueError."""
    dummy_file = tmp_path / "bad_object.joblib"
    joblib.dump({"just": "a dictionary"}, dummy_file)

    with pytest.raises(ValueError, match="not a valid News Sentiment pipeline"):
        load_pipeline(dummy_file)


def test_term_contributions_and_spectrum(trained_test_pipeline):
    """Predicting single headline must return term contributions, spectrum score, and explanation."""
    res = predict_single(
        "Quarterly earnings surge and profit expanded",
        trained_test_pipeline
    )
    assert "spectrum_score" in res
    assert isinstance(res["spectrum_score"], float)
    assert -1.0 <= res["spectrum_score"] <= 1.0
    assert "contributions" in res
    assert isinstance(res["contributions"], list)
    assert "explanation" in res
    assert len(res["explanation"]) > 0

