# Sriram R — Personal Portfolio & Data Science Showcase

> **Data Science & Python Professional**  
> *Data Analysis • Python Development • SQL Databases • Machine Learning • Data Pipelines*

[![React](https://img.shields.io/badge/React-19-61DAFB.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6.svg)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-8-646CFF.svg)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC.svg)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/pytest-31%20Passed-brightgreen.svg)](scripts/run_all_python_tests.py)
[![Verification](https://img.shields.io/badge/Portfolio%20Tests-46%2F46%20Passing-emerald.svg)](scripts/verifyPortfolio.ts)

A high-performance personal portfolio and interactive data science showcase for **Sriram R**. Features 9 production-grade analytics pipelines, an interactive project dashboard with category filters and real-time search, automated test verification, and an offline deterministic AI assistant.

---

## 🚀 Interactive Project Dashboard (9 Unique Projects)

The dashboard presents 9 distinct, working projects backed by real source code, synthetic datasets, documentation, and automated test suites.

| # | Project | Category | Technology Stack | Implementation |
|---|---|---|---|---|
| **1** | [Personal Finance & Expense Intelligence Dashboard](projects/personal-finance-dashboard/) | **Financial Analytics** | Python, Pandas, Plotly, Streamlit, pytest | [`projects/personal-finance-dashboard/`](projects/personal-finance-dashboard/) |
| **2** | [Retail Sales Analytics with SQL](projects/retail-sales-analytics/) | **SQL & Business Intelligence** | SQL, SQLite, Python, Pandas, Plotly, pytest | [`projects/retail-sales-analytics/`](projects/retail-sales-analytics/) |
| **3** | [Customer Churn Prediction](projects/customer-churn-prediction/) | **Machine Learning** | Python, Scikit-learn, Pandas, NumPy, Matplotlib, pytest | [`projects/customer-churn-prediction/`](projects/customer-churn-prediction/) |
| **4** | [E-Commerce Sales Analytics](projects/ecommerce-sales-analytics/) | **Commercial Analytics** | Python, Pandas, SQL, Plotly, Streamlit, pytest | [`projects/ecommerce-sales-analytics/`](projects/ecommerce-sales-analytics/) |
| **5** | [Data Cleaning and Quality Pipeline](projects/data-quality-pipeline/) | **Data Engineering** | Python, Pandas, SQL, pytest | [`projects/data-quality-pipeline/`](projects/data-quality-pipeline/) |
| **6** | [Python API Data Pipeline](projects/python-api-pipeline/) | **Data Engineering** | Python, REST APIs, Pandas, SQL, logging, pytest | [`projects/python-api-pipeline/`](projects/python-api-pipeline/) |
| **7** | [Business Performance Reporting Automation](projects/business-report-automation/) | **Business Intelligence** | Python, Pandas, SQL, CSV/Excel, pytest | [`projects/business-report-automation/`](projects/business-report-automation/) |
| **8** | [Student Academic Performance Analytics](project%201/) | **Data Analytics** | Python, Pandas, NumPy, Matplotlib, Seaborn, pytest | [`project 1/`](project%201/) |
| **9** | [News Sentiment & Editorial Intelligence Studio](PROJECT%202/) | **NLP & Machine Learning** | Python, Scikit-learn, Plotly, Streamlit, Pandas | [`PROJECT 2/`](PROJECT%202/) |

---

## 🌟 Key Application Features

- **Modern Glassmorphic Dark Aesthetic**: Sleek `#0B132B` and `#1C2541` dark palette, copper gold accents (`#D4A373`), responsive layouts, and interactive micro-animations.
- **Dynamic Project Dashboard**:
  - Filter pills: `All Projects (9)`, `Featured (3)`, and granular domain categories.
  - Real-time search: Instant filtering by keyword, library, or title.
  - Interactive project detail modal with problem statements, solutions, key features, and source repository links.
- **Single Source of Truth**: All website profile data, social links, education, and project records reside centrally in [`src/data/portfolio.ts`](src/data/portfolio.ts).
- **Sriram AI Chatbot**:
  - Floating assistant with suggested questions (*"Who is Sriram?"*, *"What are Sriram's skills?"*, *"Tell me about your projects."*, etc.).
  - Deterministic knowledge base in [`src/services/chatService.ts`](src/services/chatService.ts) with zero hallucinations.
  - Pluggable external LLM endpoint proxy support.
- **Education & Experience Timeline**:
  - Paavai Engineering College BE CSE (GPA 7.8), HSC (82%), SSLC (80%).
  - GDSC Namakkal participant; Corizo, Live Stream Technologies, and AICTE internships.
- **Automated Quality Assurance**:
  - 46-test automated portfolio verification suite (`scripts/verifyPortfolio.ts`).
  - Unified Python project test runner testing all 8 project suites (`scripts/run_all_python_tests.py`).

---

## 🚀 Getting Started Locally

### 1. Run the Portfolio Web App
```bash
# Install dependencies
npm install

# Start local Vite dev server
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

### 2. Run the Automated Portfolio Verification Suite
```bash
npx tsx scripts/verifyPortfolio.ts
```

### 3. Run All Python Project Tests (31 Passing Tests)
```bash
python scripts/run_all_python_tests.py
```

### 4. Build for Production
```bash
npm run build
```

---

## 📂 Repository Structure

```text
c:\protofilo\
├── projects/
│   ├── personal-finance-dashboard/   # Streamlit finance app & budget variance engine
│   ├── retail-sales-analytics/       # Relational SQLite schema, SQL queries & reports
│   ├── customer-churn-prediction/    # Scikit-learn classification & zero-leakage pipeline
│   ├── ecommerce-sales-analytics/    # E-Commerce trends & RFM customer segmentation
│   ├── data-quality-pipeline/        # Data cleaning, schema validation & IQR outlier capping
│   ├── python-api-pipeline/          # REST API pagination, retry logic & SQLite persistence
│   └── business-report-automation/   # KPI calculations & automated executive briefs
├── project 1/                        # Student academic performance analysis pipeline
├── PROJECT 2/                        # News sentiment & editorial intelligence studio (SIGNAL NOIR)
├── scripts/
│   ├── run_all_python_tests.py       # Master runner executing all Python project pytest suites
│   └── verifyPortfolio.ts            # Portfolio assertions & chatbot verification suite
├── src/
│   ├── components/                   # React components (hero, projects, skills, chatbot, etc.)
│   ├── data/portfolio.ts             # Centralized project & profile configuration
│   ├── services/chatService.ts       # Sriram AI local knowledge engine & API proxy
│   └── types/index.ts                # TypeScript data interfaces
└── tailwind.config.js                # Custom design system tokens
```

---

## 📜 License

MIT License. Designed and maintained by **Sriram R**.
