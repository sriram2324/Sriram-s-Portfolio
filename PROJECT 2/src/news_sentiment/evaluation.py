"""Evaluation metrics, baseline comparison, and visualization helpers for SIGNAL NOIR."""

from typing import Any, Dict, List, Optional
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_fscore_support,
)

from news_sentiment.config import SENTIMENT_STYLES, THEME_COLORS


def calculate_metrics(
    y_true: List[str],
    y_pred: List[str],
    labels: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Calculates comprehensive classification metrics for held-out ground truth."""
    if labels is None:
        labels = sorted(list(set(y_true) | set(y_pred)))

    acc = float(accuracy_score(y_true, y_pred))
    macro_f1 = float(f1_score(y_true, y_pred, average="macro", zero_division=0))
    weighted_f1 = float(f1_score(y_true, y_pred, average="weighted", zero_division=0))

    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, zero_division=0
    )

    per_class = {}
    for idx, lbl in enumerate(labels):
        per_class[lbl] = {
            "precision": float(round(precision[idx], 4)),
            "recall": float(round(recall[idx], 4)),
            "f1": float(round(f1[idx], 4)),
            "support": int(support[idx])
        }

    conf_mat = confusion_matrix(y_true, y_pred, labels=labels).tolist()

    return {
        "accuracy": float(round(acc, 4)),
        "macro_f1": float(round(macro_f1, 4)),
        "weighted_f1": float(round(weighted_f1, 4)),
        "labels": labels,
        "per_class": per_class,
        "confusion_matrix": conf_mat,
        "classification_report": classification_report(
            y_true, y_pred, labels=labels, output_dict=True, zero_division=0
        )
    }


def create_confusion_matrix_figure(
    matrix: List[List[int]],
    labels: List[str]
) -> go.Figure:
    """Generates an interactive Plotly heatmap styled with SIGNAL NOIR cinematic palette."""
    formatted_labels = [lbl.upper() for lbl in labels]
    z_values = np.array(matrix)

    annotations = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            is_diag = (i == j)
            font_color = "#08090c" if (is_diag and val > 10) else "#f8fafc"
            annotations.append(
                dict(
                    x=formatted_labels[j],
                    y=formatted_labels[i],
                    text=f"<b>{val}</b>",
                    font=dict(color=font_color, size=15, family="JetBrains Mono, SF Mono, monospace"),
                    showarrow=False
                )
            )

    fig = go.Figure(data=go.Heatmap(
        z=z_values,
        x=formatted_labels,
        y=formatted_labels,
        colorscale=[
            [0.0, "#08090c"],
            [0.2, "#131822"],
            [0.5, "#0e7490"],
            [0.85, "#22d3ee"],
            [1.0, "#d4ff32"]
        ],
        hoverongaps=False,
        showscale=True,
        colorbar=dict(
            title=dict(text="COUNT", font=dict(color="#94a3b8", size=10, family="monospace")),
            tickfont=dict(color="#94a3b8", size=10, family="monospace"),
            outlinecolor="rgba(255,255,255,0.08)",
            outlinewidth=1
        )
    ))

    fig.update_layout(
        title=dict(
            text="<span style='font-family: monospace; font-size: 11px; color: #22d3ee;'>// HELD-OUT VALIDATION</span><br><b>Confusion Matrix Analysis</b>",
            font=dict(size=15, color="#f8fafc"),
            x=0.02
        ),
        xaxis=dict(
            title=dict(text="PREDICTED VALENCE", font=dict(color="#94a3b8", size=11, family="monospace")),
            tickfont=dict(color="#cbd5e1", size=11, family="monospace"),
            side="bottom",
            gridcolor="rgba(255,255,255,0.04)"
        ),
        yaxis=dict(
            title=dict(text="ACTUAL GROUND TRUTH", font=dict(color="#94a3b8", size=11, family="monospace")),
            tickfont=dict(color="#cbd5e1", size=11, family="monospace"),
            autorange="reversed",
            gridcolor="rgba(255,255,255,0.04)"
        ),
        annotations=annotations,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=70, r=40, t=65, b=55),
        height=380
    )
    return fig


def create_sentiment_distribution_figure(
    counts_dict: Dict[str, int]
) -> go.Figure:
    """Creates a responsive horizontal bar chart showing sentiment breakdown."""
    classes = ["positive", "neutral", "negative"]
    counts = [counts_dict.get(c, 0) for c in classes]
    total = sum(counts)
    percentages = [f"{(c / total * 100):.1f}%" if total > 0 else "0%" for c in counts]
    colors = [SENTIMENT_STYLES[c]["color"] for c in classes]
    labels = [SENTIMENT_STYLES[c]["badge_tag"] for c in classes]

    fig = go.Figure(go.Bar(
        x=counts,
        y=labels,
        orientation="h",
        marker=dict(
            color=colors,
            line=dict(color="rgba(255,255,255,0.12)", width=1)
        ),
        text=[f"  <b>{count}</b> <span style='color: #94a3b8;'>({pct})</span>" for count, pct in zip(counts, percentages)],
        textposition="outside",
        textfont=dict(color="#f8fafc", size=12, family="monospace")
    ))

    fig.update_layout(
        title=dict(
            text="<span style='font-family: monospace; font-size: 11px; color: #d4ff32;'>// DISTRIBUTION TELEMETRY</span><br><b>Class Breakdown & Volume</b>",
            font=dict(size=14, color="#f8fafc"),
            x=0.02
        ),
        xaxis=dict(
            title=dict(text="HEADLINE VOLUME", font=dict(color="#64748b", size=10, family="monospace")),
            tickfont=dict(color="#94a3b8", size=10, family="monospace"),
            gridcolor="rgba(255, 255, 255, 0.05)",
            zeroline=False
        ),
        yaxis=dict(
            tickfont=dict(color="#f8fafc", size=12, family="monospace"),
            autorange="reversed"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=70, t=55, b=40),
        height=270
    )
    return fig


def create_timeline_trend_figure(
    df: pd.DataFrame,
    date_col: Optional[str] = None,
    sentiment_col: str = "predicted_sentiment"
) -> Optional[go.Figure]:
    """Generates a trend chart of sentiment trajectories over time or row sequence."""
    if df is None or df.empty or sentiment_col not in df.columns:
        return None

    working_df = df[df[sentiment_col].isin(["positive", "negative", "neutral"])].copy()
    if working_df.empty:
        return None

    fig = go.Figure()

    if date_col and date_col in working_df.columns:
        try:
            working_df["_parsed_date"] = pd.to_datetime(working_df[date_col], errors="coerce")
            valid_dates = working_df.dropna(subset=["_parsed_date"]).sort_values("_parsed_date")
            if not valid_dates.empty and valid_dates["_parsed_date"].nunique() > 1:
                # Group by date and count per sentiment
                daily = valid_dates.groupby([valid_dates["_parsed_date"].dt.date, sentiment_col]).size().unstack(fill_value=0)
                
                for cls_name in ["positive", "neutral", "negative"]:
                    if cls_name in daily.columns:
                        style = SENTIMENT_STYLES.get(cls_name, {})
                        fig.add_trace(go.Scatter(
                            x=daily.index,
                            y=daily[cls_name],
                            mode="lines+markers",
                            name=cls_name.upper(),
                            line=dict(color=style.get("color", "#94a3b8"), width=2),
                            marker=dict(size=5)
                        ))
                
                fig.update_layout(
                    title=dict(
                        text="<span style='font-family: monospace; font-size: 11px; color: #22d3ee;'>// TEMPORAL TELEMETRY</span><br><b>Sentiment Trajectory Over Time</b>",
                        font=dict(size=14, color="#f8fafc"),
                        x=0.02
                    ),
                    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#94a3b8", family="monospace")),
                    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#94a3b8", family="monospace")),
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(l=30, r=30, t=55, b=40),
                    height=280,
                    legend=dict(font=dict(color="#94a3b8", family="monospace"), orientation="h", y=-0.2)
                )
                return fig
        except Exception:
            pass

    # Sequence-based rolling trend fallback (window of 15)
    working_df["_row_idx"] = np.arange(len(working_df))
    window = max(5, min(20, len(working_df) // 4))

    for cls_name in ["positive", "neutral", "negative"]:
        is_cls = (working_df[sentiment_col] == cls_name).astype(float)
        rolling_series = is_cls.rolling(window=window, min_periods=1).mean()
        style = SENTIMENT_STYLES.get(cls_name, {})
        fig.add_trace(go.Scatter(
            x=working_df["_row_idx"],
            y=rolling_series,
            mode="lines",
            name=cls_name.upper(),
            line=dict(color=style.get("color", "#94a3b8"), width=2)
        ))

    fig.update_layout(
        title=dict(
            text=f"<span style='font-family: monospace; font-size: 11px; color: #22d3ee;'>// SEQUENCE ANALYSIS</span><br><b>Sequential Sentiment Flow (Rolling Window={window})</b>",
            font=dict(size=14, color="#f8fafc"),
            x=0.02
        ),
        xaxis=dict(
            title=dict(text="BATCH RECORD SEQUENCE", font=dict(color="#64748b", size=10, family="monospace")),
            gridcolor="rgba(255,255,255,0.05)",
            tickfont=dict(color="#94a3b8", family="monospace")
        ),
        yaxis=dict(
            title=dict(text="ROLLING DENSITY", font=dict(color="#64748b", size=10, family="monospace")),
            gridcolor="rgba(255,255,255,0.05)",
            tickfont=dict(color="#94a3b8", family="monospace")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=30, r=30, t=55, b=40),
        height=270,
        legend=dict(font=dict(color="#94a3b8", family="monospace"), orientation="h", y=-0.25)
    )
    return fig
