# AI Usage Record - Assignment No. 2

## 1. AI Tools Used
* Gemini (Google AI collaborator) was used for guidance on Pandas data-cleaning syntax and structural layout for test assertions.

## 2. Relevant Prompts and Summaries
* **Prompt 1:** "How do I calculate the median for age and heart rate in Pandas while ignoring missing values and out-of-range bounds?"
  * **Summary:** The response recommended filtering valid numerical ranges using boolean masks (`0 <= age <= 120`), calling `.median()` on that filtered subset, and then applying `.fillna()` to fill the missing entries.
* **Prompt 2:** "What is the best way to check for repeated patient IDs after stripping whitespace and removing exact duplicate rows?"
  * **Summary:** Suggested chaining `.drop_duplicates()` first, followed by checking `.duplicated(subset=["patient_id"])` to prevent redundant identical rows from throwing false-positive ID conflict errors.

## 3. AI Suggestion Correction / Improvement
* **Initial AI Suggestion:** The initial snippet suggested computing the imputation median on the entire column directly after converting text to numeric, without stripping extreme out-of-range bounds first (e.g., negative ages or values like 999).
* **Correction/Improvement:** I modified the logic to filter out invalid out-of-range bounds *before* calculating the statistical median. This ensures that extreme outliers do not skew the imputation values used for missing clinical records.

## 4. Testing Method
* Tested the complete implementation using a custom test suite (`test_patient_dataset.py`) containing ordinary `assert` statements and try/except blocks. 
* Verified correct schema validation, exact duplicate removal, range boundary checks, exact match on imputation counts (11 ages and 9 heart rates), error handling on conflicting patient IDs, and JSON export/reload validity.