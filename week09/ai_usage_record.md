# AI Usage Record (`AI_USE.md`)

**Course:** Programming for AI (Fall 2026)  
**Lab:** Week 9 — Introduction to Machine Learning with scikit-learn

## 1. AI Tools & Scope of Assistance

* **Tool:** Gemini (Google AI)
* **Role:** Used as an interactive technical assistant primarily for **debugging code errors, resolving runtime exceptions, and verifying error-handling logic**, in addition to syntax lookups and boundary checks.
* **Ownership:** All core code logic, pipeline structure, data validations, and assertions were written and tested manually based on lab manual requirements.

## 2. Prompts, Debugging, and Error Handling Log

### Topic 1: Resolving `ModuleNotFoundError` for Dependencies
* **User Query / Error:** `ModuleNotFoundError: No module named 'joblib'`
* **AI Guidance Received:** Recommended adding `scikit-learn` via the `uv` environment manager (`uv add scikit-learn`), which automatically provisions `joblib` into the shared virtual environment without breaking system dependencies.
* **Resolution:** Executed `uv add scikit-learn` from the course root and verified environment integrity.

### Topic 2: Debugging File-Overwrite Error in Report Export
* **User Query / Error:** *"My model comparison loop overwrote the source CSV dataset (`machines_ml.csv`) instead of creating a report."*
* **AI Guidance Received:** Identified that `DATA_PATH` was accidentally passed to `.to_csv()` instead of `REPORT_PATH`, and advised adding path verification to prevent dataset corruption.
* **Resolution:** Corrected the path target to `BASE_DIR / "reports" / "model_comparison.csv"` and implemented automatic directory creation (`mkdir(parents=True, exist_ok=True)`).

### Topic 3: Robust Error Handling for Schema and Data Validation
* **User Query:** *"How should I structure `ValueError` exceptions so the script fails gracefully if required columns or invalid target values are passed?"*
* **AI Guidance Received:** Suggested using set difference logic (`required - set(df.columns)`) and set subset checks (`set(df['fault'].unique()).issubset({0, 1})`) to catch missing columns or unexpected target values early.
* **Resolution:** Integrated strict guard clauses in Part A and Part E to handle schema mismatches before model training or prediction.

### Topic 4: Stratified Split Syntax
* **User Query:** *"How do I pass the target column to `train_test_split` so class imbalance is preserved across splits?"*
* **AI Guidance Received:** Advised using `stratify=y` with a fixed `random_state=42` seed.
* **Resolution:** Applied `stratify=y` to ensure consistent target proportions in both training and test sets.

## 3. Human Verification & Boundary Testing

To independently verify the pipeline and error handling:
1. **Validation Failures:** Tested passing a DataFrame with missing columns to verify that the custom `ValueError` exceptions trigger properly.
2. **Assertion Tests:** Added `assert abs(manual_accuracy - test_accuracy) < 1e-12` to ensure manual confusion matrix calculations match scikit-learn's accuracy score.
3. **Reproducibility Test:** Executed `uv run python week09/ml_pipeline.py` multiple times to verify deterministic model predictions and clean file exports.