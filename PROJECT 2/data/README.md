# Dataset Documentation: News Sentiment Benchmark

## 1. Overview
This repository contains two primary dataset files:
- `data/news.csv`: Curated 435-row benchmark dataset of genuine business, financial, macroeconomic, industrial, technology, and corporate governance headlines.
- `data/sample_headlines.csv`: 24-row smoke-test and batch-template CSV with balanced classes for smoke testing, UI verification, and user download templates.

## 2. Provenance and License
- **Dataset Name**: Curated Open News Sentiment Benchmark (CONS-435)
- **License**: Creative Commons Zero v1.0 Universal (`CC0 1.0` Public Domain Dedication).
- **Language**: English (US / Global Standard Business News).
- **Domains Covered**: Corporate earnings, manufacturing, supply chains, macroeconomic policy, regulatory approvals/sanctions, healthcare/pharma trials, aviation, energy transition, cybersecurity, and labor actions.
- **Access / Creation Date**: October 2026.

## 3. Schema & Required Columns
Each row contains:
- `text` (*string, required*): The headline or short news bulletin text to classify.
- `label` (*string, required for training*): The ground-truth sentiment category. Allowed classes: `positive`, `negative`, `neutral`.

## 4. Label Definitions & Annotation Policy
- **`positive`**: Headline conveys expanding revenue/earnings, business growth, contract awards, product approvals, efficiency gains, debt reductions, upgrades, or favorable operational outcomes.
  - *Example*: `"Operating profit expanded 28% year-over-year following strong demand"`
- **`negative`**: Headline conveys missed targets, operational slowdowns, bankruptcies, litigation, recalls, cyber breaches, debt downgrades, workforce reductions, or financial losses.
  - *Example*: `"Automaker recalls 450000 vehicles over potential brake system failure"`
- **`neutral`**: Headline conveys factual scheduling, administrative filings, routine reports, regulatory notices, executive transitions, or standard macroeconomic data releases without overt valence.
  - *Example*: `"Central bank keeps benchmark interest rate unchanged at policy meeting"`

## 5. Class Distribution & Quality Audit
- Total Records: 435
- Positive: 145 (33.33%)
- Negative: 145 (33.33%)
- Neutral: 145 (33.33%)
- Missing values: 0
- Exact duplicates: 0
- Near duplicates: 0

## 6. Important Caveats & Non-Goals
1. **Language Tone vs. Fact Verification**: Sentiment labels classify linguistic valence and business tone. The model does **NOT** fact-check news accuracy or verify truth.
2. **Not Market or Stock Advice**: Positive sentiment does not guarantee stock price appreciation, nor does negative sentiment guarantee decline. Market prices incorporate multifaceted forward-looking expectations.
3. **Domain Specificity**: Model is trained on English news headlines. Performance may degrade on slang, sarcasm, highly technical scientific prose, or non-English text.
