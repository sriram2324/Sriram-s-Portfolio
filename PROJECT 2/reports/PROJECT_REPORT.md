# SIGNAL NOIR: TECHNICAL BLUEPRINT & SYSTEM REPORT

**Project Identifier:** SIGNAL NOIR // Editorial Intelligence Studio  
**Level:** Production NLP Engineering • Intermediate Python • Applied Machine Learning  
**Target Schedule:** 7–10 days for production release  
**Target Cost:** ₹0 (100% open-source local dependencies, zero paid API keys)  
**Core Technologies:** Python 3.10+, Pandas, scikit-learn, Plotly, Streamlit, joblib, pytest  
**Evaluation Standard:** Zero-leakage held-out stratified test evaluation  

---

## 1. Executive Summary & Design Vision

**SIGNAL NOIR** transforms classical sentiment analysis from a toy binary classification demo into an editorial intelligence telemetry studio inspired by high-end financial terminals and investigative newsrooms.

### Design Principles:
1. **Cinematic Dark Ink & Charcoal Surfaces**: High-depth `#07080b` void foundation with `#0e1117` charcoal panels, 1px hairline dividers, and intentional negative space.
2. **Dual Technical Accent Palette**: Electric **Acid Lime** (`#d4ff32`) for bullish triggers and positive focal points; **Ice Cyan** (`#22d3ee`) for technical data and telemetry accents; **Crimson Pulse** (`#ff3b5c`) for bearish and risk events.
3. **Editorial Typography Hierarchy**: Newsreader serif for oversized editorial headlines, Plus Jakarta Sans for clean body text, and JetBrains Mono for telemetry metadata, timestamps, and model scores.
4. **Honest, Interpretable AI**: Linear feature attribution maps headline vocabulary directly to classifier coefficients ($\text{TF-IDF} \times \beta$), eliminating black-box hallucinations.
5. **Zero Data Leakage**: Stratified 80/20 train/test splitting performed before vocabulary compilation.

---

## 2. Requirements Traceability Matrix

| ID | Requirement | Architectural Implementation | Verification Result |
| :--- | :--- | :--- | :--- |
| **FR-01** | Load CSV containing `text` and `label` | `src/news_sentiment/data_validation.py` | **PASSED**: Missing columns detected with descriptive errors. |
| **FR-02** | Audit missing values, duplicates, class counts | `src/news_sentiment/preprocessing.py` | **PASSED**: Full dataset laboratory audit rendered in UI and tests. |
| **FR-03** | Clean invalid and blank rows without silent mutation | `src/news_sentiment/data_validation.py` | **PASSED**: Raw input DataFrame remains immutable; clean copy derived. |
| **FR-04** | Split before fitting transformations | `src/news_sentiment/model.py` | **PASSED**: `train_test_split` executed before `TfidfVectorizer.fit()`. |
| **FR-05** | Train, evaluate, and save pipeline atomically | `src/news_sentiment/model.py` | **PASSED**: Pipeline written via temporary files before atomic replace. |
| **FR-06** | Report held-out macro F1 and confusion matrix | `src/news_sentiment/evaluation.py` | **PASSED**: Macro F1 (0.7658), Accuracy (77.01%), and matrix saved. |
| **FR-07** | Single headline & batch CSV predictions | `src/news_sentiment/inference.py` | **PASSED**: Real-time confidence, spectrum score, and feature attribution. |
| **FR-08** | Interactive analytics dashboard | `app.py` | **PASSED**: Five dedicated studio tabs, Plotly charts, and CSV export. |
| **FR-09** | Graceful input validation | `src/news_sentiment/data_validation.py` | **PASSED**: Blank text, oversized input, and malformed files rejected safely. |
| **FR-10** | Document provenance, license, setup, limitations | `README.md` & `data/README.md` | **PASSED**: Complete data card, mathematical blueprint, and disclaimers. |

---

## 3. Machine Learning Architecture & Feature Math

### A. Sublinear TF-IDF Representation
Headlines are tokenized using word unigrams and bigrams $(1, 2)$ with a minimum document frequency of 2. Sublinear term weighting dampens the impact of repeated words:
$$\text{TF-IDF}(t, d) = (1 + \log(\text{tf}(t, d))) \cdot \log\left(\frac{1 + N}{1 + \text{df}(t)}\right) + 1$$

### B. Regularized Multiclass Logistic Regression
The classifier optimizes an L2-penalized cross-entropy loss function:
$$\min_{\beta} -\sum_{i=1}^N \sum_{c=1}^C y_{i,c} \log P(y_i = c \mid x_i) + \frac{1}{2C} \sum_{c=1}^C \|\beta_c\|_2^2$$
Inverse class frequencies are used as weights (`class_weight='balanced'`) to prevent majority-class bias.

### C. Direct Linear Feature Attribution
Because the model is linear, term importance for class $c$ is calculated directly:
$$\text{Impact}(w, c) = \text{TF-IDF}(w, d) \cdot \beta_{c, w}$$
This yields an exact, mathematically truthful list of positive and negative vocabulary cues for each classified headline.

---

## 4. Real Held-Out Evaluation Findings

Evaluated on the 20% held-out test split (87 unseen headlines from `data/news.csv`):

| Metric | Real Score | Engineering Significance |
| :--- | :---: | :--- |
| **Accuracy** | **77.01%** | 67 of 87 held-out test headlines classified correctly |
| **Macro F1** | **0.7658** | Harmonic mean weighted equally across all 3 classes |
| **Negative F1** | **0.6809** | Precision=0.8889, Recall=0.5517 (High precision on downside risk) |
| **Neutral F1** | **0.8814** | Precision=0.8667, Recall=0.8966 (Exceptional on routine notices) |
| **Positive F1** | **0.7353** | Precision=0.6410, Recall=0.8621 (High sensitivity to growth tone) |

### Test Confusion Matrix:
- **Actual Negative (29 rows)**: 16 classified Negative, 2 classified Neutral, 11 classified Positive.
- **Actual Neutral (29 rows)**: 0 classified Negative, 26 classified Neutral, 3 classified Positive.
- **Actual Positive (29 rows)**: 2 classified Negative, 2 classified Neutral, 25 classified Positive.

---

## 5. Automated Testing & Post-Test Sandbox Purging

The test runner [`scripts/test_and_clean.py`](file:///c:/protofilo/PROJECT%202/scripts/test_and_clean.py) executes 25 automated unit and integration tests across 4 test modules:
- **`tests/test_validation.py`**: 12 tests (single input, CSV validation, encoding, training schema checks).
- **`tests/test_inference.py`**: 6 tests (single prediction, confidence bounds, model reloading, term attribution, polarity spectrum).
- **`tests/test_batch.py`**: 4 tests (row count preservation, blank row handling, immutability, chart count verification).
- **`tests/test_cleanup.py`**: 3 tests (isolated temp sandbox purging, production directory protection, session state resets).

**Result**: 25 passed in 0.53 seconds with verified sandbox teardown.

---

## 6. Ten-Day Plan & Milestone Progression

| Day | Milestone Focus | Technical Deliverables |
| :--- | :--- | :--- |
| **Day 1** | Product vision, schema definitions, and dataset compilation | `data/README.md`, `data/news.csv`, `data/sample_headlines.csv` |
| **Day 2** | Robust data validation and encoding fallback engine | `src/news_sentiment/data_validation.py` |
| **Day 3** | Text normalization and statistical data auditing | `src/news_sentiment/preprocessing.py` |
| **Day 4** | Zero-leakage pipeline construction & atomic serialization | `src/news_sentiment/model.py`, `train.py` |
| **Day 5** | Held-out evaluation, metrics calculation, and confusion matrix | `src/news_sentiment/evaluation.py`, `reports/metrics.json` |
| **Day 6** | Feature attribution math and polarity spectrum scoring | `src/news_sentiment/inference.py` |
| **Day 7** | SIGNAL NOIR studio shell and editorial dark-ink design system | `app.py` |
| **Day 8** | Bulk telemetry studio, temporal trendlines, and CSV exports | Plotly visualizations, batch filters |
| **Day 9** | Ephemeral sandbox testing and automated cleanup verification | `tests/*.py`, `scripts/test_and_clean.py` |
| **Day 10** | Comprehensive documentation, project report, and portfolio release | `README.md`, `reports/PROJECT_REPORT.md` |

---

## 7. Learning Map: Post-Build Study Topics

1. **Applied NLP Pipelines**: Feature extraction, n-gram vocabularies, sublinear TF-IDF scaling, sparsity management.
2. **Machine Learning Rigor**: Zero-leakage workflows, stratified cross-validation, regularization tuning, class weighting.
3. **Interpretable AI**: Linear feature attribution vs. black-box SHAP/LIME approximations.
4. **Software Architecture**: Modular design, immutability of raw inputs, atomic file persistence, safe session resets.
5. **Quality Assurance**: Ephemeral pytest sandboxes, exception-safe teardown, path traversal defense.
6. **Responsible Deployment**: Clear separation of linguistic sentiment from fact-checking and financial forecasting.
