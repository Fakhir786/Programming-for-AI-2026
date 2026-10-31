# Assignment No. 2 - Patient Dataset Audit Toolkit
**BS Artificial Intelligence | Programming for AI (Fall 2026)**

## 1. Program Description
The Patient Dataset Audit Toolkit is a modular Python solution designed to load raw clinical records, validate schema compliance, audit quality anomalies, clean and impute invalid or missing points, and export structured audit summaries (`audit.json`) alongside standardized CSV records (`patients_clean.csv`)[cite: 1, 2]. The toolkit guarantees raw data immutability by operating entirely on isolated copies.

## 2. Purpose of Each Submitted File
* **`patient_dataset.py`**: Houses the core `PatientDataset` class, managing file parsing with `pathlib.Path`, column validation, anomaly auditing, deduplication, cleaning rules, imputation flags, and JSON export.
* **`demo.py`**: Executes the end-to-end workflow, prints terminal audit benchmarks (row counts, duplicates, and imputation totals), and writes the cleaned outputs to the `output/` directory[cite: 1].
* **`test_patient_dataset.py`**: Automated assertion test suite covering schema exceptions, row counts, range bounds, imputation tallies, conflicting ID error handling, and object immutability.
* **`data/patients_messy.csv`**: Primary input dataset containing 100 rows with intentional synthetic data quality anomalies.
* **`data/personal_cases.csv`**: Secondary personal test file checking edge cases, boundary thresholds, and department mapping variants.
* **`output/audit.json`**: Generated JSON audit summary of the original dataset structure[cite: 1, 2].
* **`output/patients_clean.csv`**: Cleaned, imputed, and standardized dataset exported without the pandas index[cite: 1, 2].

## 3. Validation, Standardization, and Cleaning Rules
* **Schema Validation**: Requires `patient_id`, `age`, `heart_rate`, and `department` columns; raises a `ValueError` if any are missing.
* **Missing Value Identification**: Treats empty strings, `"missing"`, `"N/A"`, and `"-"` as missing data during CSV ingestion.
* **Duplicate & ID Checks**: Removes exact duplicate rows. Strips whitespace from `patient_id` and raises a `ValueError` if any ID is missing, blank, or repeated with conflicting information.
* **Department Standardization**: Trims whitespace, converts text to uppercase, maps variant codes (`GEN MED`, `GENERAL MED`, `GENERAL-MED` $\rightarrow$ `GENERAL MEDICINE`; `CARDIO` $\rightarrow$ `CARDIOLOGY`), and converts missing strings (`NAN`, `NONE`, `-`, etc.) to `"Unknown"`.
* **Numeric Boundaries & Coercion**: Coerces `age` and `heart_rate` using `errors="coerce"`[cite: 2]. Invalid values or values outside valid bounds (`0–120` for age, `30–220` for heart rate) are converted to `NaN`[cite: 2].
* **Imputation**: Creates tracking flags (`age_imputed`, `heart_rate_imputed`) before filling missing numeric fields with the statistical median derived strictly from valid values[cite: 2].

## 4. Program and Test Commands
Run all commands from the project root using `uv`:
```bash
uv run python demo.py
uv run python test_patient_dataset.py