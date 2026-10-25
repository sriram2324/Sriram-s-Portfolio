"""
Student Performance Analysis - Main Pipeline Orchestrator

This script serves as the primary entry point for the entire analytical pipeline:
1. Loads the raw synthetic dataset.
2. Performs data inspection and cleaning (median imputation, deduplication, clipping).
3. Saves the cleaned data to data/cleaned_students.csv.
4. Executes exploratory data analysis and correlation computations.
5. Generates 5 high-resolution charts in the charts/ directory.
6. Writes an executive findings report to reports/findings_report.md.
7. Displays a comprehensive terminal summary.
"""

import sys
import os
import pandas as pd

# Import modular functions from src package
from src.data_loading import load_dataset, inspect_dataset, clean_dataset
from src.analysis import (
    calculate_student_averages,
    compute_summary_statistics,
    compute_correlations,
    display_eda_report,
    generate_findings_report
)
from src.visualizations import generate_all_charts


def run_pipeline(
    raw_data_path: str = "data/students.csv",
    cleaned_data_path: str = "data/cleaned_students.csv",
    charts_dir: str = "charts",
    report_path: str = "reports/findings_report.md"
) -> bool:
    """
    Execute the complete end-to-end data analysis pipeline.

    Parameters:
        raw_data_path (str): Path to input raw CSV dataset.
        cleaned_data_path (str): Path where cleaned CSV should be saved.
        charts_dir (str): Directory where charts will be saved.
        report_path (str): Path where findings markdown report will be written.

    Returns:
        bool: True if pipeline completed successfully, False otherwise.
    """
    print("\n" + "=" * 70)
    print("   STUDENT PERFORMANCE ANALYSIS - AUTOMATED PIPELINE")
    print("=" * 70)

    # ---------------------------------------------------------
    # Step 1: Load Raw Dataset
    # ---------------------------------------------------------
    print(f"\n[Step 1/5] Loading raw dataset from: {raw_data_path} ...")
    try:
        raw_df = load_dataset(raw_data_path)
        print(f"  -> Successfully loaded {len(raw_df)} records.")
    except FileNotFoundError as err:
        print(f"  [ERROR] {err}")
        print("  Please check that 'data/students.csv' exists.")
        return False
    except Exception as err:
        print(f"  [ERROR] Unexpected error while loading data: {err}")
        return False

    # ---------------------------------------------------------
    # Step 2: Clean and Validate Data
    # ---------------------------------------------------------
    print("\n[Step 2/5] Cleaning and validating dataset ...")
    try:
        cleaned_df, audit_log = clean_dataset(raw_df)
        print(f"  -> Cleaned dataset contains {len(cleaned_df)} records.")
        print("  -> Audit log summary:")
        for log_entry in audit_log:
            print(f"     * {log_entry}")

        # Ensure data directory exists and save cleaned copy
        os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)
        cleaned_df.to_csv(cleaned_data_path, index=False)
        print(f"  -> Cleaned data preserved at: {cleaned_data_path}")
    except Exception as err:
        print(f"  [ERROR] Data cleaning failed: {err}")
        return False

    # ---------------------------------------------------------
    # Step 3: Exploratory Data Analysis & Statistics
    # ---------------------------------------------------------
    print("\n[Step 3/5] Performing statistical analysis and correlations ...")
    try:
        df_analyzed = calculate_student_averages(cleaned_df)
        stats = compute_summary_statistics(df_analyzed)
        correlations = compute_correlations(df_analyzed)

        # Print EDA report to terminal
        display_eda_report(stats)
        
        print("\n  -> Correlation Coefficients:")
        print(f"     * Study Hours vs. Average Marks : {correlations['study_vs_marks']:+.4f}")
        print(f"     * Attendance vs. Average Marks  : {correlations['attendance_vs_marks']:+.4f}")
        print(f"     * Study Hours vs. Attendance    : {correlations['study_vs_attendance']:+.4f}")
    except Exception as err:
        print(f"  [ERROR] Statistical calculation failed: {err}")
        return False

    # ---------------------------------------------------------
    # Step 4: Generate High-Resolution Visualizations
    # ---------------------------------------------------------
    print(f"\n[Step 4/5] Generating 5 publication-ready charts in '{charts_dir}/' ...")
    try:
        chart_paths = generate_all_charts(df_analyzed, output_dir=charts_dir)
        for path in chart_paths:
            print(f"  -> Created: {path}")
    except Exception as err:
        print(f"  [ERROR] Visualization generation failed: {err}")
        return False

    # ---------------------------------------------------------
    # Step 5: Export Executive Findings Report
    # ---------------------------------------------------------
    print(f"\n[Step 5/5] Exporting executive findings report to: {report_path} ...")
    try:
        generate_findings_report(df_analyzed, stats, correlations, output_file=report_path)
        print("  -> Report successfully generated.")
    except Exception as err:
        print(f"  [ERROR] Report generation failed: {err}")
        return False

    print("\n" + "=" * 70)
    print("   PIPELINE EXECUTION FINISHED SUCCESSFULLY!")
    print("=" * 70)
    print("All outputs (cleaned data, charts, and executive report) are ready.\n")
    return True


if __name__ == "__main__":
    success = run_pipeline()
    if not success:
        sys.exit(1)
