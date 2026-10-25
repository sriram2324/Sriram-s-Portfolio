"""Text preprocessing and dataset auditing module for News Sentiment Analyzer."""

import re
from typing import Any, Dict, Optional
import pandas as pd


def clean_text(text: Any) -> str:
    """Conservatively normalizes news headline text.
    
    Trims whitespace and collapses multiple spaces, while carefully preserving
    punctuation, numbers, symbols ($, %, €), and sentiment cues.
    """
    if text is None:
        return ""
    text_str = str(text)
    cleaned = re.sub(r"\s+", " ", text_str).strip()
    return cleaned


def audit_dataset(
    df: pd.DataFrame,
    text_col: str = "text",
    label_col: Optional[str] = "label"
) -> Dict[str, Any]:
    """Computes comprehensive data quality and audit metrics for a news dataset.
    
    Reports:
        - row and column dimensions
        - missing and blank values
        - exact and text-level duplicates
        - label distribution and class imbalance ratio
        - text length and word count statistics
    """
    if df is None or df.empty:
        return {
            "error": "Dataset is empty.",
            "total_rows": 0,
            "total_columns": 0
        }

    total_rows = len(df)
    columns = list(df.columns)
    missing_counts = df.isnull().sum().to_dict()

    text_stats = {}
    if text_col in df.columns:
        series = df[text_col].fillna("").astype(str).str.strip()
        blank_count = int((series == "").sum())
        char_lens = series.str.len()
        word_counts = series.str.split().str.len()

        exact_duplicates = int(df.duplicated().sum())
        text_duplicates = int(series.duplicated().sum())
        lower_duplicates = int(series.str.lower().duplicated().sum())

        text_stats = {
            "text_column": text_col,
            "blank_rows": blank_count,
            "valid_rows": total_rows - blank_count,
            "exact_duplicate_rows": exact_duplicates,
            "text_duplicate_rows": text_duplicates,
            "casing_insensitive_duplicates": lower_duplicates,
            "char_length": {
                "min": int(char_lens.min()) if total_rows > 0 else 0,
                "mean": float(round(char_lens.mean(), 1)) if total_rows > 0 else 0,
                "median": float(round(char_lens.median(), 1)) if total_rows > 0 else 0,
                "max": int(char_lens.max()) if total_rows > 0 else 0,
            },
            "word_count": {
                "min": int(word_counts.min()) if total_rows > 0 else 0,
                "mean": float(round(word_counts.mean(), 1)) if total_rows > 0 else 0,
                "median": float(round(word_counts.median(), 1)) if total_rows > 0 else 0,
                "max": int(word_counts.max()) if total_rows > 0 else 0,
            }
        }

    label_stats = {}
    if label_col and label_col in df.columns:
        label_series = df[label_col].fillna("").astype(str).str.strip().str.lower()
        blank_labels = int((label_series == "").sum())
        raw_counts = label_series.value_counts().to_dict()

        valid_counts = [count for label, count in raw_counts.items() if label != ""]
        imbalance_ratio = 1.0
        if valid_counts and min(valid_counts) > 0:
            imbalance_ratio = round(max(valid_counts) / min(valid_counts), 2)

        proportions = {
            k: round(v / total_rows, 4) for k, v in raw_counts.items()
        }

        label_stats = {
            "label_column": label_col,
            "blank_labels": blank_labels,
            "distinct_classes": sorted(list(raw_counts.keys())),
            "class_counts": raw_counts,
            "class_proportions": proportions,
            "imbalance_ratio": imbalance_ratio,
        }

    return {
        "total_rows": total_rows,
        "total_columns": len(columns),
        "columns": columns,
        "missing_per_column": missing_counts,
        "text_audit": text_stats,
        "label_audit": label_stats
    }
