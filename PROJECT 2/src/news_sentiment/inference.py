"""Inference module for single-headline and batch CSV predictions.
Includes genuine linear feature attribution (TF-IDF term weights) and spectrum calculation.
"""

from typing import Any, Dict, List, Optional
import pandas as pd
from sklearn.pipeline import Pipeline

from news_sentiment.config import SENTIMENT_STYLES
from news_sentiment.data_validation import validate_headline_text
from news_sentiment.preprocessing import clean_text


def extract_term_contributions(
    text: str,
    model: Pipeline,
    pred_label: str
) -> List[Dict[str, Any]]:
    """Extracts genuine linear feature contributions (words/n-grams) towards predicted class.
    
    Formula: Impact = TF-IDF(term, text) * Classifier_Weight(class, term)
    Never invents features or hallucinated reasoning.
    """
    try:
        tfidf = model.named_steps.get("tfidf")
        classifier = model.named_steps.get("classifier")
        if not tfidf or not classifier or not hasattr(classifier, "coef_"):
            return []

        classes = list(classifier.classes_)
        if pred_label not in classes:
            return []
        class_idx = classes.index(pred_label)

        # Sparse feature vector for single text
        feature_vec = tfidf.transform([text])
        non_zero_indices = feature_vec.indices
        if len(non_zero_indices) == 0:
            return []

        feature_names = tfidf.get_feature_names_out()
        class_weights = classifier.coef_[class_idx]

        contributions = []
        for idx in non_zero_indices:
            term = str(feature_names[idx])
            tfidf_val = float(feature_vec[0, idx])
            coef = float(class_weights[idx])
            impact = tfidf_val * coef
            contributions.append({
                "term": term,
                "weight": round(coef, 3),
                "tfidf": round(tfidf_val, 3),
                "impact": round(impact, 3)
            })

        # Sort by absolute impact descending
        contributions.sort(key=lambda x: abs(x["impact"]), reverse=True)
        return contributions[:8]
    except Exception:
        return []


def generate_plain_explanation(
    pred_label: str,
    confidence: Optional[float],
    contributions: List[Dict[str, Any]]
) -> str:
    """Synthesizes an honest plain-language explanation strictly derived from model math."""
    conf_pct = f"{confidence * 100:.1f}%" if confidence is not None else "undetermined"
    
    if not contributions:
        return (
            f"Classified as {pred_label.title()} with {conf_pct} model confidence based on general vocabulary patterns. "
            "Confidence indicates statistical classifier score, not factual market truth."
        )

    # Top positive contributing terms for this class
    top_pos_terms = [c["term"] for c in contributions if c["impact"] > 0][:3]
    top_neg_terms = [c["term"] for c in contributions if c["impact"] < 0][:2]

    parts = [f"Classified as {pred_label.title()} ({conf_pct} model confidence)."]
    if top_pos_terms:
        quoted_pos = ", ".join(f"'{t}'" for t in top_pos_terms)
        parts.append(f"Primary signal driven by vocabulary cue(s): {quoted_pos}.")
    if top_neg_terms:
        quoted_neg = ", ".join(f"'{t}'" for t in top_neg_terms)
        parts.append(f"Counter-signals observed on: {quoted_neg}.")

    parts.append("Note: Model confidence reflects training vocabulary alignment, not external factuality.")
    return " ".join(parts)


def predict_single(
    text: str,
    model: Pipeline
) -> Dict[str, Any]:
    """Generates sentiment prediction, confidence scores, spectrum rating, and term attributions.
    
    Returns:
        dict containing:
            - text: normalized input headline
            - label: predicted class string ('positive', 'negative', 'neutral')
            - confidence: float score for predicted class
            - probabilities: dict of {class_name: score} sorted descending
            - spectrum_score: float in [-1.0, 1.0] representing directional polarity
            - contributions: list of {term, weight, tfidf, impact}
            - explanation: plain-language explanation of prediction
            - style: styling metadata for UI presentation
    """
    is_valid, validation_msg = validate_headline_text(text)
    if not is_valid:
        raise ValueError(validation_msg)

    cleaned = clean_text(text)
    pred_label = str(model.predict([cleaned])[0])

    probabilities: Dict[str, float] = {}
    confidence: Optional[float] = None
    spectrum_score: float = 0.0

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba([cleaned])[0]
        classifier = model.named_steps.get("classifier")
        if classifier and hasattr(classifier, "classes_"):
            classes = [str(c) for c in classifier.classes_]
            for cls_name, prob in zip(classes, probs):
                probabilities[cls_name] = round(float(prob), 4)
            probabilities = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
            confidence = probabilities.get(pred_label, round(float(max(probs)), 4))

            # Directional Polarity Spectrum in [-1.0, +1.0]
            pos_prob = probabilities.get("positive", 0.0)
            neg_prob = probabilities.get("negative", 0.0)
            spectrum_score = round(pos_prob - neg_prob, 3)

    style = SENTIMENT_STYLES.get(pred_label, {
        "color": "#94a3b8",
        "bg_color": "rgba(148, 163, 184, 0.12)",
        "border_color": "#64748b",
        "badge_tag": f"[*] {pred_label.upper()}",
        "icon": "●",
        "label": pred_label.title(),
        "tone_descriptor": "Unclassified"
    })

    contributions = extract_term_contributions(cleaned, model, pred_label)
    explanation = generate_plain_explanation(pred_label, confidence, contributions)

    return {
        "text": cleaned,
        "label": pred_label,
        "confidence": confidence,
        "probabilities": probabilities,
        "spectrum_score": spectrum_score,
        "contributions": contributions,
        "explanation": explanation,
        "style": style
    }


def predict_batch(
    df: pd.DataFrame,
    text_column: str,
    model: Pipeline
) -> pd.DataFrame:
    """Performs batch prediction on a DataFrame while preserving the raw input.
    
    Guarantees:
        - Original row order and row count are strictly preserved.
        - Blank or whitespace-only rows are skipped safely and marked as empty.
        - Prediction columns `predicted_sentiment`, model scores, and polarity spectrum added.
    """
    if df is None or df.empty:
        return pd.DataFrame()

    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in input DataFrame.")

    result_df = df.copy()
    cleaned_series = result_df[text_column].fillna("").astype(str).str.strip()
    valid_mask = cleaned_series != ""

    result_df["predicted_sentiment"] = ""
    result_df["sentiment_polarity"] = None
    
    has_proba = hasattr(model, "predict_proba")
    classes: List[str] = []
    if has_proba and "classifier" in model.named_steps:
        classifier = model.named_steps["classifier"]
        if hasattr(classifier, "classes_"):
            classes = [str(c) for c in classifier.classes_]
            for cls_name in classes:
                result_df[f"score_{cls_name}"] = None

    if valid_mask.any():
        valid_texts = cleaned_series[valid_mask].tolist()
        predictions = model.predict(valid_texts)
        result_df.loc[valid_mask, "predicted_sentiment"] = [str(p) for p in predictions]

        if has_proba and classes:
            probs = model.predict_proba(valid_texts)
            for idx, cls_name in enumerate(classes):
                col_name = f"score_{cls_name}"
                result_df.loc[valid_mask, col_name] = [round(float(p[idx]), 4) for p in probs]

            # Calculate sentiment polarity if positive and negative exist
            if "positive" in classes and "negative" in classes:
                pos_idx = classes.index("positive")
                neg_idx = classes.index("negative")
                polarities = [round(float(p[pos_idx] - p[neg_idx]), 3) for p in probs]
                result_df.loc[valid_mask, "sentiment_polarity"] = polarities

    return result_df
