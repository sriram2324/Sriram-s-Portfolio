"""CLI script for model training and hyperparameter configuration."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
from news_sentiment.config import DEFAULT_DATA_PATH, MODELS_DIR, REPORTS_DIR
from news_sentiment.model import train_and_evaluate


def parse_args():
    parser = argparse.ArgumentParser(description="Train News Sentiment Classifier")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH, help="Path to labeled CSV")
    parser.add_argument("--model-dir", type=Path, default=MODELS_DIR, help="Directory to save model")
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR, help="Directory to save metrics")
    parser.add_argument("--test-size", type=float, default=0.2, help="Fraction of held-out test data")
    parser.add_argument("--random-state", type=int, default=42, help="Seed for reproducible split")
    parser.add_argument("--min-df", type=int, default=2, help="TF-IDF min document frequency")
    parser.add_argument("--max-features", type=int, default=50000, help="TF-IDF max features")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.data.exists():
        print(f"Error: dataset file '{args.data}' does not exist.")
        sys.exit(1)

    print(f"Reading dataset: {args.data}")
    df = pd.read_csv(args.data)

    hyperparams = {
        "min_df": args.min_df,
        "max_features": args.max_features,
        "random_state": args.random_state
    }

    pipeline, metrics = train_and_evaluate(
        df=df,
        test_size=args.test_size,
        random_state=args.random_state,
        hyperparams=hyperparams,
        save_artifacts=True,
        model_dir=args.model_dir,
        reports_dir=args.reports_dir
    )

    print("\nTraining completed successfully!")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Macro F1: {metrics['macro_f1']:.4f}")


if __name__ == "__main__":
    main()
