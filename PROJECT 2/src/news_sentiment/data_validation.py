"""Data validation module for News Sentiment Analyzer.
Handles single text validation, CSV upload validation, training schema checks,
and safe encoding fallbacks.
"""

from dataclasses import dataclass
from io import BytesIO, StringIO
from pathlib import Path
from typing import Any, Tuple, Optional, Union
import pandas as pd

from news_sentiment.config import (
    MAX_HEADLINE_LENGTH,
    MAX_UPLOAD_BYTES,
    ALLOWED_FILE_EXTENSIONS,
    SUPPORTED_ENCODINGS,
    LABEL_MAPPING,
)


@dataclass
class ValidationResult:
    """Stores the outcome of CSV file validation."""
    is_valid: bool
    error_message: Optional[str]
    df_raw: Optional[pd.DataFrame]
    df_clean: Optional[pd.DataFrame]
    text_column: Optional[str]
    total_rows: int = 0
    valid_rows: int = 0
    blank_rows: int = 0
    duplicate_rows: int = 0


def validate_headline_text(
    text: Any,
    max_length: int = MAX_HEADLINE_LENGTH
) -> Tuple[bool, str]:
    """Validates single headline input text.
    
    Returns:
        (is_valid, message_or_cleaned_text)
    """
    if text is None:
        return False, "Input headline is empty. Please enter a valid news headline."

    text_str = str(text).strip()
    if not text_str:
        return False, "Input headline cannot be blank or only whitespace."

    if len(text_str) > max_length:
        return False, f"Headline is too long ({len(text_str)} chars). Maximum allowed is {max_length} characters."

    return True, text_str


def read_csv_safely(
    file_or_path: Union[str, Path, BytesIO, StringIO, Any]
) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
    """Reads a CSV from file path or file-like object using safe encoding fallback."""
    raw_content = None

    if isinstance(file_or_path, (str, Path)) and not isinstance(file_or_path, StringIO):
        path = Path(file_or_path)
        if not path.exists():
            return None, f"File not found: {path}"
        if path.suffix.lower() not in ALLOWED_FILE_EXTENSIONS:
            return None, f"Unsupported file extension '{path.suffix}'. Only .csv files are supported."
        size = path.stat().st_size
        if size == 0:
            return None, "The uploaded CSV file is empty (0 bytes)."
        if size > MAX_UPLOAD_BYTES:
            max_mb = MAX_UPLOAD_BYTES / (1024 * 1024)
            return None, f"File size exceeds the {max_mb:.0f} MB limit."
        raw_content = path.read_bytes()
    elif hasattr(file_or_path, "read"):
        raw_content = file_or_path.read()
        if hasattr(file_or_path, "seek"):
            file_or_path.seek(0)
        if not raw_content:
            return None, "The uploaded file contains no data (empty file)."
    else:
        return None, "Invalid input: expected file path or buffer object."

    # If already a string (e.g. from StringIO)
    if isinstance(raw_content, str):
        if not raw_content.strip():
            return None, "The uploaded CSV file is empty (0 bytes)."
        try:
            df = pd.read_csv(StringIO(raw_content))
            return df, None
        except Exception as err:
            return None, f"Malformed CSV structure: {str(err)}"

    # If bytes, test supported encodings
    if isinstance(raw_content, bytes):
        if len(raw_content) > MAX_UPLOAD_BYTES:
            max_mb = MAX_UPLOAD_BYTES / (1024 * 1024)
            return None, f"File size exceeds the {max_mb:.0f} MB limit."

        last_error = None
        for enc in SUPPORTED_ENCODINGS:
            try:
                text_data = raw_content.decode(enc)
                df = pd.read_csv(StringIO(text_data))
                return df, None
            except UnicodeDecodeError as err:
                last_error = err
                continue
            except Exception as err:
                return None, f"Malformed CSV structure: {str(err)}"

        return None, f"Unable to decode CSV file with supported encodings. Error: {last_error}"

    return None, "Unrecognized content format."


def validate_csv_input(
    file_or_path: Union[str, Path, BytesIO, StringIO, Any],
    text_column_override: Optional[str] = None
) -> ValidationResult:
    """Validates a CSV file for batch sentiment analysis.
    
    Never mutates the raw input dataframe.
    Returns clean DataFrame where blank rows are flagged and duplicate rows are counted.
    """
    df, error = read_csv_safely(file_or_path)
    if error or df is None:
        return ValidationResult(
            is_valid=False,
            error_message=error,
            df_raw=None,
            df_clean=None,
            text_column=None
        )

    # Immutable raw copy
    df_raw = df.copy()

    # Determine text column
    selected_col = None
    if text_column_override and text_column_override in df.columns:
        selected_col = text_column_override
    elif "text" in df.columns:
        selected_col = "text"
    elif "headline" in df.columns:
        selected_col = "headline"
    elif "news" in df.columns:
        selected_col = "news"
    else:
        # Check case-insensitive match
        for col in df.columns:
            if str(col).lower() in ["text", "headline", "news", "title", "content"]:
                selected_col = col
                break

    if not selected_col:
        cols_str = ", ".join(f"`{c}`" for c in df.columns) if len(df.columns) > 0 else "None"
        return ValidationResult(
            is_valid=False,
            error_message=(
                f"Missing required text column. The CSV must contain a column named `text` "
                f"(or `headline`). Found columns: [{cols_str}]."
            ),
            df_raw=df_raw,
            df_clean=None,
            text_column=None,
            total_rows=len(df_raw)
        )

    total_rows = len(df)
    if total_rows == 0:
        return ValidationResult(
            is_valid=False,
            error_message="The CSV file has headers but contains zero data rows.",
            df_raw=df_raw,
            df_clean=None,
            text_column=selected_col,
            total_rows=0
        )

    # Process text column safely without altering raw data
    series_clean = df[selected_col].fillna("").astype(str).str.strip()
    valid_mask = series_clean != ""
    valid_rows = int(valid_mask.sum())
    blank_rows = total_rows - valid_rows

    if valid_rows == 0:
        return ValidationResult(
            is_valid=False,
            error_message=f"All {total_rows} rows in column `{selected_col}` are blank or empty strings.",
            df_raw=df_raw,
            df_clean=None,
            text_column=selected_col,
            total_rows=total_rows,
            valid_rows=0,
            blank_rows=blank_rows
        )

    duplicate_rows = int(df.duplicated(subset=[selected_col]).sum())

    # Build clean working dataframe
    df_clean = df.copy()
    df_clean["_cleaned_text"] = series_clean
    df_clean["_is_valid_text"] = valid_mask

    return ValidationResult(
        is_valid=True,
        error_message=None,
        df_raw=df_raw,
        df_clean=df_clean,
        text_column=selected_col,
        total_rows=total_rows,
        valid_rows=valid_rows,
        blank_rows=blank_rows,
        duplicate_rows=duplicate_rows
    )


def validate_training_dataset(
    df: pd.DataFrame,
    text_col: str = "text",
    label_col: str = "label"
) -> Tuple[pd.DataFrame, dict]:
    """Validates and audits a labeled dataset for model training.
    
    Returns:
        (df_ready_for_training, audit_summary_dict)
    Raises:
        ValueError if required columns are missing or class requirements not met.
    """
    required = {text_col, label_col}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Training dataset is missing required column(s): {sorted(missing)}")

    before_count = len(df)
    working_df = df[[text_col, label_col]].copy()
    working_df[text_col] = working_df[text_col].fillna("").astype(str).str.strip()
    working_df[label_col] = working_df[label_col].fillna("").astype(str).str.strip().str.lower()

    # Drop empty rows
    valid_rows_mask = (working_df[text_col] != "") & (working_df[label_col] != "")
    working_df = working_df[valid_rows_mask]
    removed_empty = before_count - len(working_df)

    if working_df.empty:
        raise ValueError("Dataset has no valid rows after removing empty text and labels.")

    # Deduplicate text & label pairs
    before_dedup = len(working_df)
    working_df = working_df.drop_duplicates(subset=[text_col, label_col])
    duplicates_removed = before_dedup - len(working_df)

    # Normalize labels
    working_df[label_col] = working_df[label_col].map(lambda x: LABEL_MAPPING.get(x, x))

    # Inspect class counts
    class_counts = working_df[label_col].value_counts().to_dict()
    distinct_classes = sorted(list(class_counts.keys()))

    if len(distinct_classes) < 2:
        raise ValueError(
            f"At least two distinct label classes are required for training. "
            f"Found classes: {distinct_classes}."
        )

    min_class_count = min(class_counts.values())
    if min_class_count < 2:
        small_classes = [c for c, count in class_counts.items() if count < 2]
        raise ValueError(
            f"Each class requires at least 2 rows for a stratified train/test split. "
            f"Class(es) with insufficient rows: {small_classes}. Counts: {class_counts}."
        )

    audit = {
        "initial_rows": int(before_count),
        "removed_empty_rows": int(removed_empty),
        "removed_duplicate_rows": int(duplicates_removed),
        "usable_rows": int(len(working_df)),
        "classes": distinct_classes,
        "class_counts": {str(k): int(v) for k, v in class_counts.items()},
        "min_class_count": int(min_class_count),
    }

    return working_df, audit
