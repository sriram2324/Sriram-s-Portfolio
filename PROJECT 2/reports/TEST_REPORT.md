# SIGNAL NOIR: AUTOMATED TEST EXECUTION & VERIFICATION REPORT

**Project:** SIGNAL NOIR // Editorial Intelligence Studio  
**Test Suite:** Pytest Unit & Integration Suite with Guaranteed Post-Test Cleanup  
**Date of Run:** October 24, 2026  
**Execution Environment:** Windows, Python 3.14.7, pytest-9.1.1, pluggy-1.7.0  
**Command Executed:** `python scripts/test_and_clean.py`  
**Overall Result:** **25 PASSED / 0 FAILED (100% Pass Rate)**  
**Execution Duration:** 0.53 seconds  

---

## 1. Test Summary by Module

| Test Module | Tests Run | Passed | Failed | Test Coverage Focus |
| :--- | :---: | :---: | :---: | :--- |
| `tests/test_validation.py` | 12 | 12 | 0 | Headline text validation, CSV schema, empty/malformed files, training class checks |
| `tests/test_inference.py` | 6 | 6 | 0 | Single inference, confidence bounds, deterministic reload, term attribution, polarity spectrum |
| `tests/test_batch.py` | 4 | 4 | 0 | Row order preservation, blank row handling, immutability, chart count verification |
| `tests/test_cleanup.py` | 3 | 3 | 0 | Ephemeral sandbox purging, production directory protection, session state reset |
| **Total** | **25** | **25** | **0** | **100% Suite Success** |

---

## 2. Complete Test Inventory

### A. Data Validation (`tests/test_validation.py`)
1. `test_valid_headline_passes`: Verifies clean string is returned for standard text.
2. `test_blank_headline_rejected`: Verifies empty, whitespace-only, and None inputs are rejected with clear messages.
3. `test_oversized_headline_rejected`: Verifies that text exceeding the maximum length limit (1,000 characters) is blocked safely.
4. `test_missing_text_column_validation_error`: Verifies that CSVs without a `text` or `headline` column trigger a helpful error showing existing columns.
5. `test_empty_csv_handled`: Verifies 0-byte CSV files return an informative error message.
6. `test_headers_only_csv_handled`: Verifies CSVs with headers but 0 rows are cleanly identified.
7. `test_malformed_unsupported_file_handled`: Verifies non-CSV file extensions (e.g., `.xlsx`) are rejected safely.
8. `test_all_blank_rows_handled`: Verifies that a CSV whose text column consists solely of blank rows is caught.
9. `test_alternate_headline_column_supported`: Verifies automatic recognition and aliasing of `headline` column to standard schema.
10. `test_training_missing_label_column_rejected`: Verifies training raises `ValueError` if `label` column is absent.
11. `test_training_single_class_rejected`: Verifies training raises `ValueError` when dataset contains fewer than 2 distinct classes.
12. `test_training_class_counts_too_small_rejected`: Verifies datasets with classes containing < 2 rows for stratified splitting are rejected with descriptive messages.

### B. Single Inference, Attribution & Persistence (`tests/test_inference.py`)
13. `test_valid_headline_prediction_allowed_class`: Verifies inference outputs one of the allowed classes (`positive`, `negative`, `neutral`) with bounded confidence [0.0, 1.0].
14. `test_blank_input_raises_in_inference`: Verifies calling `predict_single` on whitespace raises `ValueError`.
15. `test_model_artifact_missing_handled`: Verifies loading non-existent model raises `FileNotFoundError` with clear training instructions.
16. `test_saved_model_reload_deterministic`: Verifies that deserializing a saved pipeline produces 100% identical predictions and class probabilities for fixed inputs.
17. `test_invalid_pipeline_artifact_rejected`: Verifies that non-pipeline artifacts (e.g. arbitrary dictionaries) raise a `ValueError`.
18. `test_term_contributions_and_spectrum`: Verifies that single headline prediction returns extracted term contributions, a bounded polarity spectrum score $[-1.0, 1.0]$, and a plain-language synthesis.

### C. Batch Processing & Row Alignment (`tests/test_batch.py`)
19. `test_batch_preserves_order_and_row_count`: Verifies batch predictions strictly maintain input row order and exact row count.
20. `test_blank_rows_skipped_in_batch`: Verifies blank/empty rows in CSV are not sent to model and remain empty strings without crashing.
21. `test_batch_raw_dataframe_unmutated`: Verifies that the input DataFrame passed to `predict_batch` remains completely unmutated.
22. `test_chart_totals_match_valid_predicted_rows`: Verifies that the sum of positive, negative, and neutral items in chart data matches the count of valid predicted rows.

### D. Cleanup & Session Reset (`tests/test_cleanup.py`)
23. `test_test_temp_files_removed_after_test`: Verifies that temporary test sandboxes are completely purged during teardown.
24. `test_cleanup_protects_production_data_and_models`: Verifies that cleanup logic strictly forbids deleting production directories (`data/`, `models/`, `reports/`, `src/`).
25. `test_reset_action_clears_stale_session_keys`: Verifies that `reset_streamlit_session` clears transient interactive keys without modifying persistent configuration or dictionary keys during iteration.

---

## 3. Post-Test Cleanup Verification

- **Temporary Directory:** Isolated `tmp_path` sandboxes and designated `.temp_test` root
- **Cleanup Finalizer:** Invoked within `try/finally` block inside `scripts/test_and_clean.py`
- **Result:** Temporary directories and files created during tests were removed.
- **Integrity Check:** Production files (`models/sentiment_pipeline.joblib`, `data/news.csv`, `reports/metrics.json`) remained untouched and fully intact.
- **Exit Status:** Preserved exit code `0` returned to the host environment.
