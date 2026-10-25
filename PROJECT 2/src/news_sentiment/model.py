"""Model training, serialization, loading, and held-out evaluation module.
Builds TF-IDF + Logistic Regression pipelines with strict prevention of data leakage.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import sklearn

from news_sentiment.config import (
    DEFAULT_HYPERPARAMS,
    MODELS_DIR,
    MODEL_PATH,
    METADATA_PATH,
    REPORTS_DIR,
    METRICS_PATH,
)
from news_sentiment.data_validation import validate_training_dataset


def build_pipeline(
    ngram_range: Tuple[int, int] = DEFAULT_HYPERPARAMS["ngram_range"],
    min_df: int = DEFAULT_HYPERPARAMS["min_df"],
    max_features: int = DEFAULT_HYPERPARAMS["max_features"],
    class_weight: str = DEFAULT_HYPERPARAMS["class_weight"],
    max_iter: int = DEFAULT_HYPERPARAMS["max_iter"],
    C: float = DEFAULT_HYPERPARAMS["C"],
    random_state: int = DEFAULT_HYPERPARAMS["random_state"]
) -> Pipeline:
    """Constructs a scikit-learn text classification pipeline."""
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            ngram_range=ngram_range,
            min_df=min_df,
            max_features=max_features,
            sublinear_tf=True
        )),
        ("classifier", LogisticRegression(
            C=C,
            max_iter=max_iter,
            class_weight=class_weight,
            random_state=random_state
        ))
    ])


def compute_dataset_hash(df: pd.DataFrame) -> str:
    """Computes a SHA-256 fingerprint of the text and label columns."""
    content = "".join(df["text"].astype(str) + "::" + df["label"].astype(str))
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


def train_and_evaluate(
    df: pd.DataFrame,
    test_size: float = DEFAULT_HYPERPARAMS["test_size"],
    random_state: int = DEFAULT_HYPERPARAMS["random_state"],
    hyperparams: Optional[Dict[str, Any]] = None,
    save_artifacts: bool = True,
    model_dir: Optional[Path] = None,
    reports_dir: Optional[Path] = None
) -> Tuple[Pipeline, Dict[str, Any]]:
    """Trains TF-IDF + Logistic Regression pipeline on labeled headlines.
    
    Splits data before fitting any feature transformations to guarantee zero test leakage.
    Evaluates held-out predictions and returns the trained pipeline and detailed metrics.
    """
    clean_df, audit = validate_training_dataset(df)
    params = {**DEFAULT_HYPERPARAMS, **(hyperparams or {})}

    # Stratified Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        clean_df["text"],
        clean_df["label"],
        test_size=test_size,
        random_state=random_state,
        stratify=clean_df["label"]
    )

    pipeline = build_pipeline(
        ngram_range=params.get("ngram_range", (1, 2)),
        min_df=params.get("min_df", 2),
        max_features=params.get("max_features", 50000),
        class_weight=params.get("class_weight", "balanced"),
        max_iter=params.get("max_iter", 1000),
        C=params.get("C", 1.0),
        random_state=random_state
    )

    # Fit ONLY on training data (strictly no leakage)
    pipeline.fit(X_train, y_train)

    # Evaluate on held-out test data
    y_pred = pipeline.predict(X_test)
    labels = sorted(list(clean_df["label"].unique()))

    class_report_dict = classification_report(
        y_test, y_pred, output_dict=True, zero_division=0
    )
    conf_matrix = confusion_matrix(y_test, y_pred, labels=labels).tolist()

    acc = float(accuracy_score(y_test, y_pred))
    macro_f1 = float(f1_score(y_test, y_pred, average="macro"))

    test_indices = X_test.index
    misclassified_examples: List[Dict[str, Any]] = []
    has_proba = hasattr(pipeline, "predict_proba")
    y_test_list = list(y_test)
    X_test_list = list(X_test)

    probs = pipeline.predict_proba(X_test) if has_proba else None

    for idx, (text_item, true_label, pred_label) in enumerate(zip(X_test_list, y_test_list, y_pred)):
        if true_label != pred_label:
            confidence = float(max(probs[idx])) if probs is not None else None
            misclassified_examples.append({
                "index": int(test_indices[idx]),
                "text": text_item,
                "true_label": true_label,
                "predicted_label": pred_label,
                "confidence": confidence
            })

    dataset_fingerprint = compute_dataset_hash(clean_df)
    now_iso = datetime.now(timezone.utc).isoformat()

    metrics = {
        "model_version": "1.0.0",
        "trained_at_utc": now_iso,
        "dataset_hash": dataset_fingerprint,
        "total_dataset_rows": int(len(clean_df)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "test_size": float(test_size),
        "random_state": int(random_state),
        "accuracy": acc,
        "macro_f1": macro_f1,
        "labels": labels,
        "class_counts": audit["class_counts"],
        "classification_report": class_report_dict,
        "confusion_matrix": conf_matrix,
        "confusion_matrix_labels": labels,
        "misclassified_count": len(misclassified_examples),
        "misclassified_samples": misclassified_examples[:15],
        "hyperparameters": {
            "ngram_range": list(params.get("ngram_range", (1, 2))),
            "min_df": params.get("min_df", 2),
            "max_features": params.get("max_features", 50000),
            "class_weight": str(params.get("class_weight", "balanced")),
            "C": float(params.get("C", 1.0)),
        },
        "environment": {
            "scikit_learn_version": sklearn.__version__,
            "joblib_version": joblib.__version__,
            "pandas_version": pd.__version__,
        }
    }

    if save_artifacts:
        target_model_dir = Path(model_dir) if model_dir else MODELS_DIR
        target_reports_dir = Path(reports_dir) if reports_dir else REPORTS_DIR

        target_model_dir.mkdir(parents=True, exist_ok=True)
        target_reports_dir.mkdir(parents=True, exist_ok=True)

        m_path = target_model_dir / "sentiment_pipeline.joblib"
        tmp_m_path = target_model_dir / "sentiment_pipeline.joblib.tmp"
        joblib.dump(pipeline, tmp_m_path)
        if tmp_m_path.exists():
            tmp_m_path.replace(m_path)

        meta_path = target_model_dir / "metadata.json"
        tmp_meta = target_model_dir / "metadata.json.tmp"
        tmp_meta.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        tmp_meta.replace(meta_path)

        rep_path = target_reports_dir / "metrics.json"
        tmp_rep = target_reports_dir / "metrics.json.tmp"
        tmp_rep.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
        tmp_rep.replace(rep_path)

    return pipeline, metrics


def load_pipeline(model_path: Optional[Path] = None) -> Pipeline:
    """Loads a verified scikit-learn pipeline artifact.
    
    Raises:
        FileNotFoundError if the model artifact is missing.
        ValueError if the file is invalid or lacks the expected pipeline steps.
    """
    path = Path(model_path) if model_path else MODEL_PATH
    if not path.exists():
        raise FileNotFoundError(
            f"Model artifact not found at '{path}'. Please train the model first by running "
            "`python train.py` or clicking 'Train Model' in the dashboard."
        )

    try:
        pipeline = joblib.load(path)
    except Exception as exc:
        raise ValueError(f"Failed to deserialize model artifact from '{path}': {str(exc)}")

    if not isinstance(pipeline, Pipeline) or "tfidf" not in pipeline.named_steps or "classifier" not in pipeline.named_steps:
        raise ValueError(
            f"The artifact at '{path}' is not a valid News Sentiment pipeline. "
            "Expected Pipeline with 'tfidf' and 'classifier' steps."
        )

    return pipeline


def get_model_metadata(model_dir: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    """Retrieves saved metadata.json if available."""
    target_dir = Path(model_dir) if model_dir else MODELS_DIR
    meta_file = target_dir / "metadata.json"
    if not meta_file.exists():
        return None
    try:
        return json.loads(meta_file.read_text(encoding="utf-8"))
    except Exception:
        return None
