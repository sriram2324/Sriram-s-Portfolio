"""
Automated Test Suite for Student Performance Analysis

This test suite uses pytest to verify:
1. Dataset loading and missing file error handling.
2. Presence of all mandatory schema columns.
3. Permitted value boundaries (marks 0-100, attendance 0-100, study hours 0-12).
4. Mathematical accuracy of student average calculations and pass flags.
5. Graceful handling of empty or invalid data inputs.
"""

import os
import pytest
import pandas as pd
import numpy as np

from src.data_loading import load_dataset, clean_dataset
from src.analysis import (
    calculate_student_averages,
    compute_summary_statistics,
    compute_correlations,
    SUBJECT_COLUMNS
)


@pytest.fixture
def sample_raw_dataframe():
    """Fixture providing a mock raw DataFrame with known edge cases."""
    return pd.DataFrame({
        'student_id': ['STD_001', 'STD_002', 'STD_002', 'STD_003'],
        'study_hours': [4.0, np.nan, 5.0, 10.0],
        'attendance': [80.0, 90.0, 90.0, 60.0],
        'math_marks': [70.0, 80.0, 80.0, 105.0],  # 105 is out of bounds
        'science_marks': [60.0, np.nan, 75.0, 90.0],
        'english_marks': [50.0, 85.0, 85.0, 80.0]
    })


def test_load_dataset_success():
    """Verify that the raw CSV dataset loads successfully and is non-empty."""
    filepath = os.path.join("data", "students.csv")
    assert os.path.exists(filepath), f"File {filepath} does not exist."
    
    df = load_dataset(filepath)
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 100, f"Expected >= 100 records, got {len(df)}"


def test_load_dataset_file_not_found():
    """Verify that an invalid filepath raises a FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_dataset("non_existent_path/fake_data.csv")


def test_required_columns_exist():
    """Verify that all required columns are present in the dataset."""
    expected_columns = {
        'student_id',
        'study_hours',
        'attendance',
        'math_marks',
        'science_marks',
        'english_marks'
    }
    df = load_dataset(os.path.join("data", "students.csv"))
    assert expected_columns.issubset(set(df.columns)), (
        f"Missing columns: {expected_columns - set(df.columns)}"
    )


def test_data_cleaning_and_permitted_ranges(sample_raw_dataframe):
    """
    Verify that cleaning eliminates duplicates, imputes missing values,
    and enforces permitted numerical boundaries.
    """
    cleaned_df, audit_log = clean_dataset(sample_raw_dataframe)

    # 1. Deduplication check (should drop 1 duplicate)
    assert len(cleaned_df) == 3
    assert cleaned_df['student_id'].duplicated().sum() == 0

    # 2. No missing values remaining
    assert cleaned_df.isnull().sum().sum() == 0

    # 3. Permitted range check for marks (0 to 100)
    for col in SUBJECT_COLUMNS:
        assert (cleaned_df[col] >= 0.0).all(), f"Found negative values in {col}"
        assert (cleaned_df[col] <= 100.0).all(), f"Found values > 100 in {col}"

    # 4. Study hours permitted range (0 to 12)
    assert (cleaned_df['study_hours'] >= 0.0).all()
    assert (cleaned_df['study_hours'] <= 12.0).all()

    # 5. Attendance permitted range (0 to 100)
    assert (cleaned_df['attendance'] >= 0.0).all()
    assert (cleaned_df['attendance'] <= 100.0).all()

    # 6. Audit log should contain logged corrections
    assert len(audit_log) > 0


def test_calculate_student_averages_math_accuracy():
    """Verify the mathematical correctness of row-wise subject averages and pass rule."""
    test_df = pd.DataFrame({
        'student_id': ['STD_A', 'STD_B'],
        'study_hours': [5.0, 2.0],
        'attendance': [80.0, 50.0],
        'math_marks': [90.0, 40.0],
        'science_marks': [80.0, 45.0],
        'english_marks': [70.0, 50.0]
    })
    
    result_df = calculate_student_averages(test_df, pass_threshold=50.0)

    # Student A: (90 + 80 + 70) / 3 = 80.0 -> Passed
    assert result_df.loc[0, 'average_marks'] == 80.0
    assert result_df.loc[0, 'passed'] is True or result_df.loc[0, 'passed'] == 1

    # Student B: (40 + 45 + 50) / 3 = 45.0 -> Failed (< 50)
    assert result_df.loc[1, 'average_marks'] == 45.0
    assert result_df.loc[1, 'passed'] is False or result_df.loc[1, 'passed'] == 0


def test_empty_dataframe_raises_value_error():
    """Verify that computing summary stats on an empty DataFrame raises ValueError."""
    empty_df = pd.DataFrame(columns=['student_id', 'average_marks', 'passed'] + SUBJECT_COLUMNS)
    with pytest.raises(ValueError, match="Cannot compute statistics on an empty dataset."):
        compute_summary_statistics(empty_df)
