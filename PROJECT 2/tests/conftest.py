"""Pytest fixtures for News Sentiment Analyzer.
Guarantees isolated temporary test directories and clean teardowns.
"""

from pathlib import Path
import sys
import pytest
import pandas as pd

# Ensure src is importable
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from news_sentiment.model import build_pipeline
from news_sentiment.cleanup import clean_temp_directory


@pytest.fixture
def synthetic_labeled_df() -> pd.DataFrame:
    """Provides a synthetic balanced labeled dataset for fast isolated testing."""
    return pd.DataFrame({
        "text": [
            "Company quarterly earnings surge 50 percent beating market expectations",
            "Operating profit expanded following strong international sales",
            "Dividend payout increased by 20 percent on robust cash flows",
            "Firm announces major breakthrough in renewable battery technology",
            "Shares drop heavily after disappointing quarterly guidance",
            "Automaker recalls thousands of vehicles over severe brake failure",
            "Factory announces immediate production shutdown due to supply shortage",
            "Debt downgraded to junk status following debt default",
            "Central bank leaves benchmark interest rate unchanged at meeting",
            "Company issues scheduled annual sustainability report to shareholders",
            "Board of directors schedules regular annual meeting for next month",
            "Ministry publishes routine preliminary macroeconomic statistics"
        ],
        "label": [
            "positive", "positive", "positive", "positive",
            "negative", "negative", "negative", "negative",
            "neutral", "neutral", "neutral", "neutral"
        ]
    })


@pytest.fixture
def trained_test_pipeline(synthetic_labeled_df):
    """Provides a trained pipeline fitted only on synthetic fixture data."""
    pipe = build_pipeline(ngram_range=(1, 2), min_df=1, random_state=42)
    pipe.fit(synthetic_labeled_df["text"], synthetic_labeled_df["label"])
    return pipe


@pytest.fixture
def isolated_temp_env(tmp_path: Path):
    """Provides an isolated temporary directory tree that is wiped on teardown."""
    temp_dir = tmp_path / "sandbox"
    temp_dir.mkdir(parents=True, exist_ok=True)
    yield temp_dir
    # Teardown
    clean_temp_directory(temp_dir=temp_dir, allowed_root=tmp_path)
