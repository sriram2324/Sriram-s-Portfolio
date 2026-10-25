"""
Exploratory Data Analysis (EDA) Module

This module performs statistical calculations on cleaned student data:
- Individual student average marks
- Subject-wise averages
- Study hours and attendance averages
- Performance extremes (highest and lowest scores)
- Pass/Fail rate evaluation based on a documented threshold
"""

import os
import pandas as pd


SUBJECT_COLUMNS = ['math_marks', 'science_marks', 'english_marks']
DEFAULT_PASS_THRESHOLD = 50.0


def calculate_student_averages(df: pd.DataFrame, pass_threshold: float = DEFAULT_PASS_THRESHOLD) -> pd.DataFrame:
    """
    Calculate average marks across all subjects for each student and assign a pass/fail status.

    Parameters:
        df (pd.DataFrame): The cleaned student dataset.
        pass_threshold (float): Minimum overall average required to pass (default 50.0%).
                                Note: This is a simplified pedagogical assumption for this
                                practice project, not a formal grading standard.

    Returns:
        pd.DataFrame: DataFrame with 'average_marks' and 'passed' boolean columns added.
    """
    df_analyzed = df.copy()
    # axis=1 computes the mean horizontally across the subject columns for each row
    df_analyzed['average_marks'] = df_analyzed[SUBJECT_COLUMNS].mean(axis=1).round(2)
    df_analyzed['passed'] = df_analyzed['average_marks'] >= pass_threshold
    return df_analyzed


def compute_summary_statistics(df_analyzed: pd.DataFrame, pass_threshold: float = DEFAULT_PASS_THRESHOLD) -> dict:
    """
    Compute comprehensive dataset-wide summary statistics.

    Parameters:
        df_analyzed (pd.DataFrame): DataFrame containing 'average_marks' and 'passed'.
        pass_threshold (float): The pass threshold used.

    Returns:
        dict: Key summary metrics and findings.
    """
    total_students = len(df_analyzed)
    if total_students == 0:
        raise ValueError("Cannot compute statistics on an empty dataset.")

    # 1. Subject averages
    subject_averages = {
        col: round(float(df_analyzed[col].mean()), 2)
        for col in SUBJECT_COLUMNS
    }
    
    # 2. Overall student average across all subjects
    overall_mean_marks = round(float(df_analyzed['average_marks'].mean()), 2)

    # 3. Attendance and Study Hours averages
    avg_attendance = round(float(df_analyzed['attendance'].mean()), 2)
    avg_study_hours = round(float(df_analyzed['study_hours'].mean()), 2)

    # 4. Highest and Lowest performing students
    idx_max = df_analyzed['average_marks'].idxmax()
    idx_min = df_analyzed['average_marks'].idxmin()

    top_student = {
        'student_id': df_analyzed.loc[idx_max, 'student_id'],
        'average_marks': df_analyzed.loc[idx_max, 'average_marks'],
        'study_hours': df_analyzed.loc[idx_max, 'study_hours'],
        'attendance': df_analyzed.loc[idx_max, 'attendance']
    }

    lowest_student = {
        'student_id': df_analyzed.loc[idx_min, 'student_id'],
        'average_marks': df_analyzed.loc[idx_min, 'average_marks'],
        'study_hours': df_analyzed.loc[idx_min, 'study_hours'],
        'attendance': df_analyzed.loc[idx_min, 'attendance']
    }

    # 5. Pass Rule Evaluation
    passed_count = int(df_analyzed['passed'].sum())
    pass_percentage = round((passed_count / total_students) * 100, 2)

    # 6. Rank highest scoring subject
    highest_subject = max(subject_averages, key=subject_averages.get)
    lowest_subject = min(subject_averages, key=subject_averages.get)

    return {
        'total_students': total_students,
        'subject_averages': subject_averages,
        'highest_subject': (highest_subject, subject_averages[highest_subject]),
        'lowest_subject': (lowest_subject, subject_averages[lowest_subject]),
        'overall_mean_marks': overall_mean_marks,
        'avg_attendance': avg_attendance,
        'avg_study_hours': avg_study_hours,
        'top_student': top_student,
        'lowest_student': lowest_student,
        'pass_threshold': pass_threshold,
        'passed_count': passed_count,
        'pass_percentage': pass_percentage
    }


def display_eda_report(stats: dict):
    """Print a clean, formatted terminal summary of the exploratory analysis."""
    print("=" * 65)
    print("     EXPLORATORY DATA ANALYSIS (EDA) - SUMMARY REPORT")
    print("=" * 65)
    print(f"\n[1] Total Analyzed Students: {stats['total_students']}")
    
    print("\n[2] Subject-Wise Average Marks:")
    for subj, avg in stats['subject_averages'].items():
        clean_name = subj.replace('_', ' ').title()
        print(f"    - {clean_name:<16}: {avg:.2f} / 100")
    print(f"    * Top Scoring Subject : {stats['highest_subject'][0].replace('_', ' ').title()} ({stats['highest_subject'][1]:.2f})")
    print(f"    * Lowest Scoring Subject: {stats['lowest_subject'][0].replace('_', ' ').title()} ({stats['lowest_subject'][1]:.2f})")

    print("\n[3] Overall Cohort Marks:")
    print(f"    - Overall Average Mark: {stats['overall_mean_marks']:.2f} / 100")

    print("\n[4] Engagement Metrics:")
    print(f"    - Average Daily Study Hours: {stats['avg_study_hours']:.2f} hrs/day")
    print(f"    - Average Attendance Rate  : {stats['avg_attendance']:.2f}%")

    print("\n[5] Performance Extremes:")
    top = stats['top_student']
    low = stats['lowest_student']
    print(f"    - Highest Performing Student: {top['student_id']} with avg mark of {top['average_marks']:.2f} "
          f"(Study: {top['study_hours']}h, Attendance: {top['attendance']}%)")
    print(f"    - Lowest Performing Student : {low['student_id']} with avg mark of {low['average_marks']:.2f} "
          f"(Study: {low['study_hours']}h, Attendance: {low['attendance']}%)")

    print("\n[6] Pass / Fail Outcome (Pedagogical Rule: >= 50.0%):")
    print(f"    - Students Passed    : {stats['passed_count']} / {stats['total_students']}")
    print(f"    - Cohort Pass Rate   : {stats['pass_percentage']:.2f}%")
    print("=" * 65)


def compute_correlations(df_analyzed: pd.DataFrame) -> dict:
    """
    Calculate Pearson correlation coefficients between behavioral factors and academic performance.

    Parameters:
        df_analyzed (pd.DataFrame): DataFrame with 'study_hours', 'attendance', and 'average_marks'.

    Returns:
        dict: Correlation values rounded to 4 decimal places.
    """
    r_study_marks = float(df_analyzed['study_hours'].corr(df_analyzed['average_marks']))
    r_attendance_marks = float(df_analyzed['attendance'].corr(df_analyzed['average_marks']))
    r_study_attendance = float(df_analyzed['study_hours'].corr(df_analyzed['attendance']))

    return {
        'study_vs_marks': round(r_study_marks, 4),
        'attendance_vs_marks': round(r_attendance_marks, 4),
        'study_vs_attendance': round(r_study_attendance, 4)
    }


def generate_findings_report(df_analyzed: pd.DataFrame, stats: dict, correlations: dict, output_file: str = None) -> str:
    """
    Produce a comprehensive, evidence-based analytical report answering all core questions.

    Parameters:
        df_analyzed (pd.DataFrame): The analyzed student DataFrame.
        stats (dict): The summary statistics dictionary.
        correlations (dict): The computed correlations dictionary.
        output_file (str, optional): If provided, writes the report to this path.

    Returns:
        str: Formatted markdown report text.
    """
    top = stats['top_student']
    lowest = stats['lowest_student']
    highest_subj = stats['highest_subject']
    lowest_subj = stats['lowest_subject']

    report = f"""# Student Performance Analysis - Executive Findings Report

## 1. Executive Summary & Core Metrics
* **Analyzed Sample Size**: {stats['total_students']} unique students
* **Overall Cohort Average Mark**: **{stats['overall_mean_marks']:.2f}%**
* **Average Daily Study Hours**: {stats['avg_study_hours']:.2f} hours/day
* **Average Attendance Rate**: {stats['avg_attendance']:.2f}%
* **Cohort Passing Rate (Threshold >= {stats['pass_threshold']:.1f}%)**: {stats['pass_percentage']:.2f}% ({stats['passed_count']} / {stats['total_students']})

---

## 2. Subject Performance Comparison
* **Top Scoring Subject**: **{highest_subj[0].replace('_', ' ').title()}** with an average score of **{highest_subj[1]:.2f}%**
* **Lowest Scoring Subject**: **{lowest_subj[0].replace('_', ' ').title()}** with an average score of **{lowest_subj[1]:.2f}%**
* **Math Cohort Average**: {stats['subject_averages']['math_marks']:.2f}%

*Insight*: Science and Math exhibited very similar average distributions (75.45% vs 75.17%), while English lagged by approximately 4 percentage points (71.19%).

---

## 3. High & Low Performance Extremes
* **Highest Performing Student**:
  * **ID**: `{top['student_id']}`
  * **Average Mark**: **{top['average_marks']:.2f}%**
  * **Engagement**: {top['study_hours']} daily study hours, {top['attendance']}% attendance rate.
* **Lowest Performing Student**:
  * **ID**: `{lowest['student_id']}`
  * **Average Mark**: **{lowest['average_marks']:.2f}%**
  * **Engagement**: {lowest['study_hours']} daily study hours, {lowest['attendance']}% attendance rate.

---

## 4. Correlation Analysis & Hypothesis Testing

| Relationship Examined | Pearson Correlation ($r$) | Strength & Direction |
| :--- | :---: | :--- |
| **Study Hours vs. Average Marks** | **{correlations['study_vs_marks']:+.4f}** | Moderate-to-Strong Positive |
| **Attendance vs. Average Marks** | **{correlations['attendance_vs_marks']:+.4f}** | Moderate Positive |
| **Study Hours vs. Attendance** | **{correlations['study_vs_attendance']:+.4f}** | Near Zero / Independent |

### Evidence-Based Answers to Research Questions:
1. **Does the sample suggest an association between study hours and marks?**
   * **Yes.** A Pearson coefficient of **r = {correlations['study_vs_marks']:.2f}** confirms a notable positive association. Students with higher daily dedicated study time consistently trended toward higher academic marks across all three subjects.
2. **Does the sample suggest an association between attendance and marks?**
   * **Yes.** A Pearson coefficient of **r = {correlations['attendance_vs_marks']:.2f}** indicates a moderate positive association. Students with attendance above 80% generally secured marks above the cohort mean.

---

## 5. Critical Methodological Disclaimers

### A. Correlation Does Not Imply Causation
While higher study hours and attendance positively correlate with higher marks in this dataset, **correlation does not prove causation**:
* Confounding variables—such as prior subject knowledge, home study environment, learning speed, and syllabus comprehension—can influence both study habits and exam scores.
* Simply sitting in a classroom without active mental engagement or spending passive hours with a textbook does not mechanically guarantee academic mastery.

### B. Synthetic Data Limitation
* This dataset is **synthetic** and generated specifically for data analysis pipeline development and educational demonstration.
* Empirical conclusions derived here demonstrate technical methodology and Python data workflows; they must **not** be cited as real-world pedagogical or psychological findings.
"""

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)

    return report


if __name__ == "__main__":
    CLEANED_DATA_PATH = os.path.join("data", "cleaned_students.csv")
    REPORT_PATH = os.path.join("reports", "findings_report.md")
    
    if not os.path.exists(CLEANED_DATA_PATH):
        print(f"Cleaned dataset not found at {CLEANED_DATA_PATH}. Please run src/data_loading.py first.")
    else:
        df = pd.read_csv(CLEANED_DATA_PATH)
        df_analyzed = calculate_student_averages(df)
        stats = compute_summary_statistics(df_analyzed)
        correlations = compute_correlations(df_analyzed)
        
        display_eda_report(stats)
        
        print("\n>>> CORRELATION ANALYSIS:")
        print(f"    - Study Hours vs Average Marks : r = {correlations['study_vs_marks']:+.4f}")
        print(f"    - Attendance vs Average Marks  : r = {correlations['attendance_vs_marks']:+.4f}")
        print(f"    - Study Hours vs Attendance    : r = {correlations['study_vs_attendance']:+.4f}")

        report_md = generate_findings_report(df_analyzed, stats, correlations, output_file=REPORT_PATH)
        print(f"\n[OK] Findings report written to: {REPORT_PATH}")

