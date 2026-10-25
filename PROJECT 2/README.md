# SIGNAL NOIR // Editorial Intelligence Studio

An editorial-grade NLP intelligence platform that extracts linguistic sentiment signals, directional polarity, and mathematical feature attributions from news headlines and financial dispatches.

Inspired by modern financial terminals, investigative journalism, and dark-ink telemetry consoles. Built with Python, Pandas, scikit-learn, Plotly, and Streamlit, featuring sublinear TF-IDF feature representation, regularized Logistic Regression, zero data leakage, and automated test sandbox cleanup.

---

## ⚡ The Product Vision

```
     ___ ___ ____ _   _    _    _       _   _  ___ ___ ____  
    / __|_ _/ ___| \ | |  / \  | |     | \ | |/ _ \_ _|  _ \ 
    \__ \| | |  _|  \| | / _ \ | |     |  \| | | | | || |_) |
     ___) | | |_| | |\  |/ ___ \| |___  | |\  | |_| | ||  _ < 
    |____/___\____|_| \_/_/   \_\_____| |_| \_|\___/___|_| \_\
    EDITORIAL INTELLIGENCE STUDIO // NLP SENTIMENT TELEMETRY
```

> **"Read the signal. Understand the sentiment."**  
> SIGNAL NOIR is not a toy demo. It is an art-directed intelligence studio that deconstructs the vocabulary of market announcements, quantifies directional sentiment valence, and exposes genuine linear feature attribution.

---

## 🌟 Core Studio Capabilities

1. **Headline Telemetry Terminal**:
   - Single-headline real-time classification into `[+] POSITIVE`, `[-] NEGATIVE`, or `[=] NEUTRAL`.
   - Directional Polarity Spectrum meter calibrated from `-1.000` (Bearish / Contracting) to `+1.000` (Bullish / Expanding).
   - **Feature Attribution Reel**: Real-time extraction of top contributing n-grams ($Impact = \text{TF-IDF} \times \beta$) showing exact vocabulary drivers.
   - Plain-Language Telemetry Synthesis derived strictly from model math without hallucination.
   - Session activity reel tracking recently classified headlines with quick reload.

2. **Bulk Telemetry & Batch Analytics**:
   - Drag-and-drop CSV ingestion with automatic column detection (`text`, `headline`, or custom mapping).
   - Schema auditing: row counts, valid headlines, blank row skipping, and exact duplicate detection.
   - Plotly dark-terminal distribution charts and sequential/temporal rolling trendlines.
   - Real-time keyword search, sentiment filtering, polarity sorting, and one-click CSV export.

3. **Dataset Laboratory & Quality Audit**:
   - Live audit of the 435-row curated benchmark dataset or user-uploaded corpora.
   - Tracks class balance, imbalance ratios, character/word length distributions, and stratification feasibility.

4. **Model Laboratory & Held-Out Evaluation**:
   - Held-out test performance telemetry: **77.01% Accuracy**, **0.7658 Macro F1**.
   - Interactive Plotly Confusion Matrix with customized dark-ink colorscale.
   - Per-class Precision, Recall, F1-Score, and Support breakdown.
   - Error Analysis Table exposing misclassified test samples for model refinement.
   - Live retraining drawer with configurable test split size, n-gram ranges, and regularization inverse $C$.

5. **Safe Session Reset & Sandboxed Cleanup**:
   - Instant workspace clearing that purges transient session state while preserving persistent model artifacts and datasets on disk.
   - Automated testing executes inside isolated sandboxes with guaranteed cleanup on teardown.

---

## 📊 Dataset Specification & Provenance

- **Dataset Identifier**: Curated Open News Sentiment Benchmark (CONS-435)
- **License**: Creative Commons Zero v1.0 Universal (`CC0 1.0` Public Domain Dedication)
- **Total Records**: 435 curated headlines spanning corporate earnings, central banks, supply chains, mergers, labor actions, and energy transition.
- **Class Balance**: 145 positive (33.33%), 145 negative (33.33%), 145 neutral (33.33%) — completely balanced.
- **Quality Audit**: 0 nulls, 0 blank rows, 0 duplicate records.

---

## 📈 Held-Out Model Evaluation Results

> Evaluated strictly on the **20% held-out test split (87 unseen headlines)**. The TF-IDF vectorizer and Logistic Regression classifier were fitted **exclusively on the 348 training rows** to ensure zero data leakage.

| Metric | Real Measured Score | Notes |
| :--- | :---: | :--- |
| **Accuracy** | **77.01%** | 67 of 87 held-out headlines correctly classified |
| **Macro F1** | **0.7658** | Balanced unweighted harmonic mean |
| **Training Records (80%)** | 348 | Used to train vectorizer vocabulary and weights |
| **Test Records (20%)** | 87 | Held-out validation sample |

### Per-Class Performance:

| Class | Precision | Recall | F1-Score | Support (N) |
| :--- | :---: | :---: | :---: | :---: |
| **[-] Negative** | 0.8889 | 0.5517 | 0.6809 | 29 |
| **[=] Neutral** | 0.8667 | 0.8966 | 0.8814 | 29 |
| **[+] Positive** | 0.6410 | 0.8621 | 0.7353 | 29 |

### Confusion Matrix (Test Split):
```
Actual \ Predicted   Negative   Neutral   Positive
Negative                16         2         11
Neutral                  0        26          3
Positive                 2         2         25
```

---

## 📐 Machine Learning Architecture & Feature Attribution

### 1. Vectorization
$$\text{TF-IDF}(t, d) = (1 + \log(\text{tf}(t, d))) \cdot \log\left(\frac{1 + N}{1 + \text{df}(t)}\right) + 1$$
Features are constrained to word unigrams and bigrams $(1, 2)$ with $\text{min\_df}=2$ to capture short sentiment idioms (e.g. *"record profit"*, *"misses estimates"*).

### 2. Classification
$$\hat{y} = \arg\max_{c} \left( \sum_{w \in d} \text{tfidf}(w, d) \cdot \beta_{c, w} + \text{intercept}_c \right)$$
Using L2-regularized Multiclass Logistic Regression with balanced class weighting.

### 3. Feature Attribution Derivation
$$\text{Impact}(w, c) = \text{TF-IDF}(w, d) \cdot \beta_{c, w}$$
This yields genuine, mathematically truthful term attribution for every headline without black-box approximations.

---

## 💻 Installation & Quickstart

### Prerequisites
- Python 3.10+ (Tested on Python 3.14)
- Local terminal environment

```bash
# 1. Install dependencies
python -m pip install -r requirements.txt

# 2. Train baseline model (generates models/sentiment_pipeline.joblib)
python train.py

# 3. Launch SIGNAL NOIR Studio
streamlit run app.py
```
Open **http://localhost:8501** in your browser.

---

## 🧪 Automated Testing & Sandbox Cleanup

Execute the full automated test suite with isolated sandbox verification:
```bash
python scripts/test_and_clean.py
```
- **25 of 25 tests pass in ~0.53 seconds**.
- All fixtures execute in isolated temporary directories (`tmp_path`).
- Post-test finalizers guarantee that no temporary test files remain on disk.
- Production models, source code, datasets, and reports are protected.

---

## ⚠️ Ethical Boundaries & Disclaimers

1. **Linguistic Valence vs. Factual Truth**: SIGNAL NOIR evaluates language tone and vocabulary choice. It does **NOT** determine whether a news story is factually true or false.
2. **Not Financial Advice**: Positive headline sentiment does not imply stock prices will rise; equity prices discount complex future expectations and macroeconomic variables.
3. **Context & Sarcasm Deficit**: Sarcasm, deep legal nuances, and industry jargon can lead to misclassifications.
4. **100% Local Privacy**: Runs entirely on the host machine. No text or queries are sent to external cloud APIs.

---

## 📂 Repository Layout

```
news-sentiment-analyzer/
├── app.py                     # SIGNAL NOIR Streamlit Studio Dashboard
├── train.py                   # Zero-leakage CLI training entrypoint
├── requirements.txt           # Pinned dependencies
├── README.md                  # Comprehensive product guide
├── .gitignore                 # Exclusion rules
├── src/
│   └── news_sentiment/
│       ├── __init__.py        # Package initialization
│       ├── config.py          # SIGNAL NOIR tokens, colors, paths
│       ├── data_validation.py # Schema checks & encoding fallbacks
│       ├── preprocessing.py   # Text cleaning & statistical audits
│       ├── model.py           # Pipeline construction & atomic saving
│       ├── inference.py       # Single & batch prediction + term attribution
│       ├── evaluation.py      # Metrics, confusion matrix, timeline charts
│       └── cleanup.py         # Ephemeral sandbox cleanup & session resets
├── scripts/
│   ├── generate_dataset.py    # Curated benchmark dataset generator
│   ├── train_model.py         # Configurable CLI training script
│   └── test_and_clean.py      # Automated test runner with guaranteed cleanup
├── data/
│   ├── README.md              # Dataset documentation & data card
│   ├── news.csv               # 435-row curated benchmark corpus
│   └── sample_headlines.csv   # 24-row smoke-test and template CSV
├── models/
│   ├── README.md              # Artifact security instructions
│   ├── sentiment_pipeline.joblib # Serialized scikit-learn pipeline
│   └── metadata.json          # Model metadata & evaluation scores
├── reports/
│   ├── README.md              # Reports documentation
│   ├── metrics.json           # Evaluation metrics output
│   ├── PROJECT_REPORT.md      # Engineering blueprint & handbook
│   └── TEST_REPORT.md         # Automated test audit report
└── tests/
    ├── conftest.py            # Isolated fixtures & synthetic data
    ├── test_validation.py     # Schema, empty, and malformed input tests
    ├── test_inference.py      # Inference, attribution, and reload tests
    ├── test_batch.py          # Batch alignment & chart count tests
    └── test_cleanup.py        # Sandbox isolation & session reset tests
```
