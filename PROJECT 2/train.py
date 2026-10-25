"""Root training entrypoint for News Sentiment Analyzer.
Trains a TF-IDF + Logistic Regression pipeline on labeled news headlines,
evaluates on held-out test data, and persists pipeline and metrics.
"""

from pathlib import Path
import sys

# Ensure src is in Python path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import pandas as pd
from news_sentiment.config import (
    DEFAULT_DATA_PATH,
    MODELS_DIR,
    REPORTS_DIR,
    MODEL_PATH,
    METRICS_PATH,
)
from news_sentiment.model import train_and_evaluate


def main():
    data_path = DEFAULT_DATA_PATH
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])

    if not data_path.exists():
        print(f"Error: Dataset not found at '{data_path}'.")
        print("Please place your labeled CSV with 'text' and 'label' columns at 'data/news.csv'.")
        sys.exit(1)

    print(f"Loading labeled news dataset from: {data_path}")
    df = pd.read_csv(data_path)

    try:
        pipeline, metrics = train_and_evaluate(
            df=df,
            test_size=0.2,
            random_state=42,
            save_artifacts=True,
            model_dir=MODELS_DIR,
            reports_dir=REPORTS_DIR
        )
    except Exception as exc:
        print(f"Training failed: {exc}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print(" MODEL TRAINING AND EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print(f"Saved model pipeline : {MODEL_PATH}")
    print(f"Saved metrics report : {METRICS_PATH}")
    print(f"Usable records       : {metrics['total_dataset_rows']}")
    print(f"Train split rows     : {metrics['train_rows']}")
    print(f"Test split rows      : {metrics['test_rows']}")
    print(f"Held-out Accuracy    : {metrics['accuracy']:.4f}")
    print(f"Held-out Macro F1    : {metrics['macro_f1']:.4f}")
    print("-" * 60)
    print("Classification Report (Held-Out Test Set):")
    rep = metrics["classification_report"]
    for lbl in metrics["labels"]:
        p = rep[lbl]["precision"]
        r = rep[lbl]["recall"]
        f = rep[lbl]["f1-score"]
        s = rep[lbl]["support"]
        print(f"  Class '{lbl:<8}': Precision={p:.4f}  Recall={r:.4f}  F1={f:.4f}  Support={s}")
    print("-" * 60)
    print(f"Confusion Matrix (labels: {metrics['confusion_matrix_labels']}):")
    for row in metrics["confusion_matrix"]:
        print(f"  {row}")
    print("=" * 60)


if __name__ == "__main__":
    main()
