# Python REST API Ingestion Pipeline

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Storage-SQLite-003B57.svg)](https://www.sqlite.org/)
[![Testing](https://img.shields.io/badge/pytest-Passing-brightgreen.svg)](tests/)

A resilient, production-grade Python data ingestion pipeline that interfaces with public REST APIs. It provides automated pagination, network timeout resilience, exponential backoff retries, schema normalization, and relational SQLite persistence with structured standard logging.

---

## 🌟 Key Features

1. **REST API Ingestion with Public Endpoints**:
   - Interfaces with publicly accessible open REST APIs (`JSONPlaceholder`).
   - Zero private API keys or sensitive secrets required.
2. **Resilience & Fault Tolerance**:
   - Configurable timeout thresholds and exponential backoff retry cycles on network failure or HTTP 429 rate limits.
3. **Pagination & Schema Normalization**:
   - Traverses multi-page API responses, validates required payload attributes, and filters malformed payloads.
4. **Relational Database Persistence**:
   - Structured SQLite table persistence with `INSERT OR REPLACE` upsert mechanics to guard against duplicate ingest.
5. **Standardized Logging & Automated Tests**:
   - Built-in Python `logging` tracing pipeline lifecycle events and unit tests using `pytest` and `unittest.mock`.

---

## 🛠️ Technology Stack

- **Core**: Python 3.10+
- **HTTP Client**: `requests`
- **Data Manipulation**: `pandas`
- **Relational Storage**: `sqlite3`
- **Testing**: `pytest`, `unittest.mock`

---

## 🚀 Setup & Execution

```bash
# Run unit tests
python -m pytest tests/
```
