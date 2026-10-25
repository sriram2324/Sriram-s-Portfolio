"""
Data Visualization Module

This module generates five professional, publication-ready charts
illustrating student performance trends, correlations, and distributions.
All charts are saved to the charts/ directory with proper labels and styling.
"""

import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend suitable for headless scripts
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_visual_style():
    """Apply modern, clean aesthetics to Matplotlib and Seaborn charts."""
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.titlesize': 16
    })


def plot_distribution_of_marks(df: pd.DataFrame, output_dir: str = "charts") -> str:
    """
    Chart 1: Distribution of Average Marks (Histogram + KDE).
    Explains the spread of scores across the cohort.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    mean_val = df['average_marks'].mean()
    median_val = df['average_marks'].median()

    sns.histplot(
        df['average_marks'],
        kde=True,
        color="#2b5c8f",
        bins=12,
        ax=ax,
        edgecolor="white",
        alpha=0.85
    )

    ax.axvline(mean_val, color="#d9534f", linestyle="--", linewidth=2, label=f"Mean: {mean_val:.1f}")
    ax.axvline(median_val, color="#5cb85c", linestyle=":", linewidth=2, label=f"Median: {median_val:.1f}")

    ax.set_title("Distribution of Student Average Marks", weight='bold', pad=12)
    ax.set_xlabel("Average Marks (%)")
    ax.set_ylabel("Student Count")
    ax.legend(frameon=True)

    plt.tight_layout()
    output_path = os.path.join(output_dir, "1_distribution_of_marks.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def plot_study_hours_vs_marks(df: pd.DataFrame, output_dir: str = "charts") -> str:
    """
    Chart 2: Study Hours vs. Average Marks (Scatter Plot + Regression Trendline).
    Explores correlation between study time and academic outcomes.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    corr = df['study_hours'].corr(df['average_marks'])

    sns.regplot(
        data=df,
        x="study_hours",
        y="average_marks",
        ax=ax,
        scatter_kws={"color": "#1f77b4", "alpha": 0.75, "s": 50},
        line_kws={"color": "#d62728", "linewidth": 2}
    )

    ax.set_title(f"Study Hours vs. Average Marks (Pearson r = {corr:.2f})", weight='bold', pad=12)
    ax.set_xlabel("Daily Study Hours (hrs/day)")
    ax.set_ylabel("Average Marks (%)")

    plt.tight_layout()
    output_path = os.path.join(output_dir, "2_study_hours_vs_marks.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def plot_attendance_vs_marks(df: pd.DataFrame, output_dir: str = "charts") -> str:
    """
    Chart 3: Attendance vs. Average Marks (Scatter Plot + Regression Trendline).
    Explores correlation between class attendance and academic outcomes.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    corr = df['attendance'].corr(df['average_marks'])

    sns.regplot(
        data=df,
        x="attendance",
        y="average_marks",
        ax=ax,
        scatter_kws={"color": "#2ca02c", "alpha": 0.75, "s": 50},
        line_kws={"color": "#ff7f0e", "linewidth": 2}
    )

    ax.set_title(f"Attendance Rate vs. Average Marks (Pearson r = {corr:.2f})", weight='bold', pad=12)
    ax.set_xlabel("Attendance Rate (%)")
    ax.set_ylabel("Average Marks (%)")

    plt.tight_layout()
    output_path = os.path.join(output_dir, "3_attendance_vs_marks.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def plot_subject_averages(df: pd.DataFrame, output_dir: str = "charts") -> str:
    """
    Chart 4: Average Marks by Subject (Bar Chart).
    Compares cohort performance across Math, Science, and English.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    subject_map = {
        'math_marks': 'Math',
        'science_marks': 'Science',
        'english_marks': 'English'
    }
    
    means = [df[col].mean() for col in subject_map.keys()]
    labels = list(subject_map.values())
    colors = ["#4c72b0", "#55a868", "#c44e52"]

    bars = ax.bar(labels, means, color=colors, width=0.55, edgecolor="none")

    # Annotate value atop each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.1f}%",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha='center', va='bottom', weight='bold'
        )

    ax.set_title("Cohort Average Marks by Subject", weight='bold', pad=12)
    ax.set_ylabel("Average Marks (%)")
    ax.set_ylim(0, 100)

    plt.tight_layout()
    output_path = os.path.join(output_dir, "4_subject_averages.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def plot_top_10_students(df: pd.DataFrame, output_dir: str = "charts") -> str:
    """
    Chart 5: Top 10 Students by Average Marks (Horizontal Bar Chart).
    Highlights highest achievers in descending order.
    """
    fig, ax = plt.subplots(figsize=(9, 5.5))
    
    top_10 = df.nlargest(10, 'average_marks').sort_values('average_marks', ascending=True)

    bars = ax.barh(top_10['student_id'], top_10['average_marks'], color="#3470a3", edgecolor="none", height=0.65)

    for bar in bars:
        width = bar.get_width()
        ax.annotate(
            f" {width:.1f}%",
            xy=(width, bar.get_y() + bar.get_height() / 2),
            xytext=(3, 0),
            textcoords="offset points",
            ha='left', va='center', weight='bold'
        )

    ax.set_title("Top 10 Students by Average Marks", weight='bold', pad=12)
    ax.set_xlabel("Average Marks (%)")
    ax.set_ylabel("Student ID")
    ax.set_xlim(0, 105)

    plt.tight_layout()
    output_path = os.path.join(output_dir, "5_top_10_students.png")
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path


def generate_all_charts(df: pd.DataFrame, output_dir: str = "charts") -> list[str]:
    """Generates and saves all 5 required charts."""
    os.makedirs(output_dir, exist_ok=True)
    set_visual_style()

    paths = [
        plot_distribution_of_marks(df, output_dir),
        plot_study_hours_vs_marks(df, output_dir),
        plot_attendance_vs_marks(df, output_dir),
        plot_subject_averages(df, output_dir),
        plot_top_10_students(df, output_dir)
    ]
    return paths


if __name__ == "__main__":
    from analysis import calculate_student_averages
    
    CLEANED_DATA_PATH = os.path.join("data", "cleaned_students.csv")
    if not os.path.exists(CLEANED_DATA_PATH):
        print(f"Cleaned dataset not found at {CLEANED_DATA_PATH}. Run src/data_loading.py first.")
    else:
        df = pd.read_csv(CLEANED_DATA_PATH)
        df_analyzed = calculate_student_averages(df)
        print("Generating charts...")
        saved_charts = generate_all_charts(df_analyzed, output_dir="charts")
        print("\n[OK] All 5 charts generated successfully:")
        for path in saved_charts:
            print(f"  * {path}")
