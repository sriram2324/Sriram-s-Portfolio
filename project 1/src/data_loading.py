"""
Data Loading and Inspection Module

This module provides functions to load the raw students dataset,
inspect its dimensions, view summary statistics, and check for
anomalies (missing values, duplicates, and out-of-range marks).
"""

import os
import pandas as pd


def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Load student dataset from a CSV file.

    Parameters:
        filepath (str): The relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found at: {filepath}")
    
    df = pd.read_csv(filepath)
    return df


def inspect_dataset(df: pd.DataFrame) -> dict:
    """
    Perform initial inspection on the DataFrame and return summary metrics.

    Parameters:
        df (pd.DataFrame): The DataFrame to inspect.

    Returns:
        dict: A dictionary containing inspection findings.
    """
    print("=" * 60)
    print("  STUDENT DATASET - INITIAL INSPECTION REPORT")
    print("=" * 60)

    # 1. Dataset Dimensions (Rows and Columns)
    num_rows, num_cols = df.shape
    print(f"\n[1] Dimensions: {num_rows} rows x {num_cols} columns")

    # 2. First 5 records (head)
    print("\n[2] First 5 Records (df.head()):")
    print(df.head())

    # 3. Last 5 records (tail)
    print("\n[3] Last 5 Records (df.tail()):")
    print(df.tail())

    # 4. Data Types and Non-Null Counts (df.info equivalent)
    print("\n[4] Column Data Types:")
    for col, dtype in df.dtypes.items():
        print(f"  - {col}: {dtype}")

    # 5. Descriptive Statistics
    print("\n[5] Summary Statistics (df.describe()):")
    print(df.describe())

    # 6. Missing Values Check
    missing_counts = df.isnull().sum()
    print("\n[6] Missing Values (df.isnull().sum()):")
    for col, count in missing_counts.items():
        print(f"  - {col}: {count} missing")

    # 7. Duplicate Records Check (by student_id)
    duplicate_ids = df[df.duplicated(subset=['student_id'], keep=False)]
    print(f"\n[7] Duplicate Student IDs: {len(duplicate_ids)} found")
    if not duplicate_ids.empty:
        print(duplicate_ids[['student_id', 'study_hours', 'attendance']])

    # 8. Range Validation Checks
    mark_cols = ['math_marks', 'science_marks', 'english_marks']
    out_of_range_marks = df[
        (df[mark_cols] < 0).any(axis=1) | (df[mark_cols] > 100).any(axis=1)
    ]
    print(f"\n[8] Out-of-Range Subject Marks (outside 0-100): {len(out_of_range_marks)} record(s)")
    if not out_of_range_marks.empty:
        print(out_of_range_marks[['student_id'] + mark_cols])

    print("\n" + "=" * 60)
    print("  INSPECTION COMPLETED")
    print("=" * 60)

    return {
        "rows": num_rows,
        "cols": num_cols,
        "missing_values": missing_counts.to_dict(),
        "duplicate_count": len(duplicate_ids),
        "out_of_range_count": len(out_of_range_marks)
    }


def clean_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """
    Clean the dataset using explicit, logged validation rules:
    1. Removes duplicate student IDs (keeping the first occurrence).
    2. Imputes missing numerical values using column median.
    3. Clips/corrects out-of-bounds marks (0-100) and logs any fixes.
    4. Preserves the original DataFrame by working on a copy.

    Parameters:
        df (pd.DataFrame): The raw DataFrame.

    Returns:
        tuple[pd.DataFrame, list[str]]: The cleaned DataFrame and an audit log of changes.
    """
    cleaned_df = df.copy()
    audit_log = []

    # 1. Handle Duplicate Student IDs
    initial_count = len(cleaned_df)
    duplicate_mask = cleaned_df.duplicated(subset=['student_id'], keep='first')
    num_duplicates = duplicate_mask.sum()
    if num_duplicates > 0:
        dup_ids = cleaned_df.loc[duplicate_mask, 'student_id'].tolist()
        cleaned_df = cleaned_df.drop_duplicates(subset=['student_id'], keep='first')
        audit_log.append(
            f"DUPLICATE REMOVAL: Removed {num_duplicates} duplicate record(s) for ID(s): {dup_ids}. "
            f"Rows reduced from {initial_count} to {len(cleaned_df)}."
        )

    # 2. Handle Missing Values via Median Imputation
    num_cols = ['study_hours', 'attendance', 'math_marks', 'science_marks', 'english_marks']
    for col in num_cols:
        missing_count = cleaned_df[col].isnull().sum()
        if missing_count > 0:
            median_val = round(cleaned_df[col].median(), 1)
            cleaned_df[col] = cleaned_df[col].fillna(median_val)
            audit_log.append(
                f"MISSING VALUE IMPUTATION: Filled {missing_count} missing value(s) in '{col}' "
                f"with column median ({median_val})."
            )

    # 3. Validate and Clip Out-of-Range Subject Marks (0 - 100)
    mark_cols = ['math_marks', 'science_marks', 'english_marks']
    for col in mark_cols:
        invalid_high = cleaned_df[cleaned_df[col] > 100.0]
        invalid_low = cleaned_df[cleaned_df[col] < 0.0]

        for idx, row in invalid_high.iterrows():
            orig_val = row[col]
            cleaned_df.loc[idx, col] = 100.0
            audit_log.append(
                f"RANGE CORRECTION: {row['student_id']} {col} was {orig_val} (> 100). Clipped to 100.0."
            )

        for idx, row in invalid_low.iterrows():
            orig_val = row[col]
            cleaned_df.loc[idx, col] = 0.0
            audit_log.append(
                f"RANGE CORRECTION: {row['student_id']} {col} was {orig_val} (< 0). Clipped to 0.0."
            )

    # 4. Validate Study Hours (0 - 12) & Attendance (0 - 100)
    invalid_study = cleaned_df[(cleaned_df['study_hours'] < 0) | (cleaned_df['study_hours'] > 12)]
    invalid_attend = cleaned_df[(cleaned_df['attendance'] < 0) | (cleaned_df['attendance'] > 100)]
    if not invalid_study.empty:
        audit_log.append(f"WARNING: {len(invalid_study)} student(s) have study hours outside 0-12 range.")
    if not invalid_attend.empty:
        audit_log.append(f"WARNING: {len(invalid_attend)} student(s) have attendance outside 0-100% range.")

    return cleaned_df, audit_log


if __name__ == "__main__":
    DATA_PATH = os.path.join("data", "students.csv")
    CLEANED_DATA_PATH = os.path.join("data", "cleaned_students.csv")
    
    try:
        raw_df = load_dataset(DATA_PATH)
        print(">>> RUNNING INITIAL INSPECTION ON RAW DATA:")
        inspect_dataset(raw_df)

        print("\n>>> PERFORMING DATA CLEANING:")
        cleaned_df, cleaning_log = clean_dataset(raw_df)

        print("\n[CLEANING AUDIT LOG]")
        for entry in cleaning_log:
            print(f"  * {entry}")

        # Save the cleaned dataset without overwriting the original raw dataset
        cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)
        print(f"\n[OK] Cleaned dataset saved to: {CLEANED_DATA_PATH} ({len(cleaned_df)} records)")

        print("\n>>> RE-INSPECTING CLEANED DATA:")
        inspect_dataset(cleaned_df)

    except FileNotFoundError as err:
        print(f"Error: {err}")

