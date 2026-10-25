"""Tests for batch CSV processing, row alignment, and chart metrics."""

import pandas as pd
import pytest

from news_sentiment.config import ALLOWED_LABELS
from news_sentiment.inference import predict_batch
from news_sentiment.evaluation import create_sentiment_distribution_figure


def test_batch_preserves_order_and_row_count(trained_test_pipeline):
    """Batch prediction must preserve the original row order and total row count."""
    df_input = pd.DataFrame({
        "headline_id": [101, 102, 103, 104, 105],
        "text": [
            "Company reports record operating profit",
            "Shares drop heavily after disappointing quarter",
            "Central bank schedules regular monetary meeting",
            "Strong customer demand drives quarterly growth",
            "Automaker recalls defective vehicles"
        ],
        "category": ["Finance", "Finance", "Macro", "Retail", "Auto"]
    })

    result_df = predict_batch(df_input, text_column="text", model=trained_test_pipeline)

    assert len(result_df) == len(df_input)
    assert list(result_df["headline_id"]) == [101, 102, 103, 104, 105]
    assert "predicted_sentiment" in result_df.columns
    for pred in result_df["predicted_sentiment"]:
        assert pred in ALLOWED_LABELS


def test_blank_rows_skipped_in_batch(trained_test_pipeline):
    """Blank or whitespace-only rows must be skipped and never sent to the model."""
    df_input = pd.DataFrame({
        "text": [
            "Quarterly profit surged 30 percent",
            "",
            "   ",
            "Severe supply chain disruption forces plant shutdown",
            None
        ]
    })

    result_df = predict_batch(df_input, text_column="text", model=trained_test_pipeline)

    assert len(result_df) == 5
    # Row 0 and 3 are valid
    assert result_df.loc[0, "predicted_sentiment"] in ALLOWED_LABELS
    assert result_df.loc[3, "predicted_sentiment"] in ALLOWED_LABELS

    # Rows 1, 2, and 4 must NOT be predicted
    assert result_df.loc[1, "predicted_sentiment"] == ""
    assert result_df.loc[2, "predicted_sentiment"] == ""
    assert result_df.loc[4, "predicted_sentiment"] == ""


def test_batch_raw_dataframe_unmutated(trained_test_pipeline):
    """The original raw DataFrame passed into predict_batch must not be mutated."""
    df_original = pd.DataFrame({
        "text": ["Headline A", "Headline B"],
        "metadata": ["meta1", "meta2"]
    })
    original_cols = list(df_original.columns)

    _ = predict_batch(df_original, text_column="text", model=trained_test_pipeline)

    assert list(df_original.columns) == original_cols
    assert "predicted_sentiment" not in df_original.columns


def test_chart_totals_match_valid_predicted_rows(trained_test_pipeline):
    """Sum of sentiment counts in chart data must exactly match valid predicted rows."""
    df_input = pd.DataFrame({
        "text": [
            "Company profit hits record high",
            "Shares drop on missed expectations",
            "Central bank leaves rates unchanged",
            "Another positive earnings announcement",
            ""  # blank row
        ]
    })

    result_df = predict_batch(df_input, text_column="text", model=trained_test_pipeline)
    valid_predictions = result_df[result_df["predicted_sentiment"] != ""]["predicted_sentiment"]
    counts = valid_predictions.value_counts().to_dict()

    total_in_chart = sum(counts.values())
    assert total_in_chart == 4  # 4 valid rows out of 5

    fig = create_sentiment_distribution_figure(counts)
    assert fig is not None
    assert fig.data[0].orientation == "h"
