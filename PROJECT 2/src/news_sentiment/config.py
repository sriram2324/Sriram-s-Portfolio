"""Configuration settings and design tokens for SIGNAL NOIR.
Editorial intelligence studio and NLP text classification platform.
"""

from pathlib import Path

# Workspace Root & Core Paths
PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
TESTS_DIR = PROJECT_ROOT / "tests"
TEMP_DIR = PROJECT_ROOT / ".temp_test"

# Default Model Paths
MODEL_PATH = MODELS_DIR / "sentiment_pipeline.joblib"
METADATA_PATH = MODELS_DIR / "metadata.json"
METRICS_PATH = REPORTS_DIR / "metrics.json"
DEFAULT_DATA_PATH = DATA_DIR / "news.csv"
SAMPLE_DATA_PATH = DATA_DIR / "sample_headlines.csv"

# Product Brand Tokens
APP_NAME = "SIGNAL NOIR"
APP_TAGLINE = "Editorial Intelligence Studio // NLP Telemetry"
APP_VERSION = "2.0.0"

# Sentiment Classes & Normalization
ALLOWED_LABELS = ["negative", "neutral", "positive"]
LABEL_MAPPING = {
    "pos": "positive",
    "positive": "positive",
    "+1": "positive",
    "1": "positive",
    "neg": "negative",
    "negative": "negative",
    "-1": "negative",
    "neu": "neutral",
    "neutral": "neutral",
    "0": "neutral"
}

# Validation Limits
MAX_HEADLINE_LENGTH = 1000
MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB
ALLOWED_FILE_EXTENSIONS = [".csv"]
SUPPORTED_ENCODINGS = ["utf-8", "utf-8-sig", "latin-1", "cp1252"]

# ML Pipeline Hyperparameters
DEFAULT_HYPERPARAMS = {
    "ngram_range": (1, 2),
    "min_df": 2,
    "max_features": 50000,
    "sublinear_tf": True,
    "max_iter": 1000,
    "C": 1.0,
    "class_weight": "balanced",
    "random_state": 42,
    "test_size": 0.2
}

# Editorial Studio Visual Identity Tokens
# Deep ink & charcoal surfaces with electric acid-lime and ice-cyan accents
THEME_COLORS = {
    "void": "#08090c",          # Deepest ink black
    "surface": "#0f1218",       # Charcoal base panel
    "surface_elevated": "#171b24", # Elevated card
    "hairline": "rgba(255, 255, 255, 0.08)", # 1px divider
    "hairline_bright": "rgba(255, 255, 255, 0.16)",
    "text_primary": "#f8fafc",  # Warm off-white
    "text_secondary": "#94a3b8", # Muted technical slate
    "text_dim": "#475569",
    "acid_lime": "#d4ff32",     # Electric high-signal trigger / positive highlight
    "ice_cyan": "#22d3ee",      # Telemetry & analysis data accent
    "crimson_pulse": "#ff3b5c", # High-valence negative warning
    "amber_signal": "#fbbf24",  # Warning / neutral alert
}

SENTIMENT_STYLES = {
    "positive": {
        "color": "#d4ff32",       # Electric Acid Lime
        "bg_color": "rgba(212, 255, 50, 0.08)",
        "border_color": "rgba(212, 255, 50, 0.35)",
        "glow": "0 0 20px rgba(212, 255, 50, 0.2)",
        "badge_tag": "[+] POSITIVE",
        "icon": "▲",
        "label": "Positive",
        "tone_descriptor": "Bullish / Expanding"
    },
    "neutral": {
        "color": "#22d3ee",       # Ice Cyan / Titanium
        "bg_color": "rgba(34, 211, 238, 0.08)",
        "border_color": "rgba(34, 211, 238, 0.35)",
        "glow": "0 0 20px rgba(34, 211, 238, 0.15)",
        "badge_tag": "[=] NEUTRAL",
        "icon": "■",
        "label": "Neutral",
        "tone_descriptor": "Factual / Administrative"
    },
    "negative": {
        "color": "#ff3b5c",       # Searing Crimson Pulse
        "bg_color": "rgba(255, 59, 92, 0.08)",
        "border_color": "rgba(255, 59, 92, 0.35)",
        "glow": "0 0 20px rgba(255, 59, 92, 0.2)",
        "badge_tag": "[-] NEGATIVE",
        "icon": "▼",
        "label": "Negative",
        "tone_descriptor": "Bearish / Contracting"
    }
}
