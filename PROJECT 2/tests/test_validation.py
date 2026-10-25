"""Tests for data validation and schema verification."""

from io import StringIO
from pathlib import Path
import pandas as pd
import pytest

from news_sentiment.data_validation import (
    validate_headline_text,
    validate_csv_input,
    validate_training_dataset,
)


def test_valid_headline_passes():
    """Valid text should pass validation and return stripped string."""
    is_valid, msg = validate_headline_text("  Central bank cuts interest rate by 25 bps  ")
    assert is_valid is True
    assert msg == "Central bank cuts interest rate by 25 bps"


def test_blank_headline_rejected():
    """Blank or whitespace-only headlines must be rejected with a clear message."""
    for blank_val in ["", "   ", "\n\t", None]:
        is_valid, msg = validate_headline_text(blank_val)
        assert is_valid is False
        assert "blank" in msg.lower() or "empty" in msg.lower()


def test_oversized_headline_rejected():
    """Headlines exceeding max length must be rejected safely."""
    huge_text = "Headline " * 200  # > 1000 chars
    is_valid, msg = validate_headline_text(huge_text, max_length=500)
    assert is_valid is False
    assert "too long" in msg.lower()


def test_missing_text_column_validation_error():
    """CSV missing a text column must fail with a helpful error showing present columns."""
    csv_data = StringIO("id,sentiment,author\n1,positive,Alice\n2,neutral,Bob\n")
    res = validate_csv_input(csv_data)
    assert res.is_valid is False
    assert "Missing required text column" in res.error_message
    assert "`id`" in res.error_message


def test_empty_csv_handled(tmp_path: Path):
    """Empty CSV files (0 bytes) must produce a clean user-facing error."""
    empty_file = tmp_path / "empty.csv"
    empty_file.write_bytes(b"")
    res = validate_csv_input(empty_file)
    assert res.is_valid is False
    assert "empty" in res.error_message.lower()


def test_headers_only_csv_handled():
    """A CSV with headers but no data rows must fail with a clear message."""
    csv_data = StringIO("text,date\n")
    res = validate_csv_input(csv_data)
    assert res.is_valid is False
    assert "zero data rows" in res.error_message.lower()


def test_malformed_unsupported_file_handled(tmp_path: Path):
    """Unsupported non-CSV extensions or binary junk must be rejected gracefully."""
    bad_file = tmp_path / "data.xlsx"
    bad_file.write_text("dummy")
    res = validate_csv_input(bad_file)
    assert res.is_valid is False
    assert "Unsupported file extension" in res.error_message


def test_all_blank_rows_handled():
    """A CSV whose text column contains only blanks should be rejected."""
    csv_data = StringIO("text,author\n   ,Alice\n\"\",Bob\n")
    res = validate_csv_input(csv_data)
    assert res.is_valid is False
    assert "blank or empty" in res.error_message.lower()


def test_alternate_headline_column_supported():
    """CSV with 'headline' instead of 'text' should be recognized automatically."""
    csv_data = StringIO("headline,source\nTech firm raises guidance,Reuters\n")
    res = validate_csv_input(csv_data)
    assert res.is_valid is True
    assert res.text_column == "headline"
    assert res.valid_rows == 1


def test_training_missing_label_column_rejected():
    """Training validation must raise ValueError if 'label' column is missing."""
    df = pd.DataFrame({"text": ["Headline A", "Headline B"]})
    with pytest.raises(ValueError, match="missing required column"):
        validate_training_dataset(df)


def test_training_single_class_rejected():
    """Training validation must raise ValueError if fewer than 2 classes are present."""
    df = pd.DataFrame({
        "text": ["Headline A", "Headline B", "Headline C"],
        "label": ["positive", "positive", "positive"]
    })
    with pytest.raises(ValueError, match="At least two distinct label classes"):
        validate_training_dataset(df)


def test_training_class_counts_too_small_rejected():
    """Training validation must reject datasets where any class has < 2 rows for stratified split."""
    df = pd.DataFrame({
        "text": ["Good 1", "Good 2", "Good 3", "Bad 1"],
        "label": ["positive", "positive", "positive", "negative"]
    })
    with pytest.raises(ValueError, match="requires at least 2 rows"):
        validate_training_dataset(df)
