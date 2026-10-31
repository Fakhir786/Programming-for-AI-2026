# Week 9 Lab: Introduction to Machine Learning with scikit-learn
**BS Artificial Intelligence | Programming for AI (Fall 2026)**

## 1. Overview
This project implements a reproducible binary classification pipeline using `scikit-learn` to predict machine equipment faults (`1` for fault, `0` for normal) based on physical sensor metrics (`temp_c`, `vibration`, `runtime`, and `pressure`).

## 2. Directory Structure
```
week09/
├── data/
│   └── machines_ml.csv         # Sensor dataset
├── models/
│   └── machine_predictor.joblib # Serialized model bundle (model + feature layout)
├── reports/
│   ├── model_comparison.csv    # Accuracy vs max_depth experiment results
│   └── confusion_matrix.png    # Visualization of evaluation matrix
├── ml_pipeline.py              # End-to-end executable ML pipeline
├── README.md                   # Project documentation
└── AI_USE.md                   # Record of AI usage & prompt log
```

## 3. Dataset & Method
- **Input Features ($X$):** `temp_c` (°C), `vibration` (mm/s), `runtime` (hours), `pressure` (bar).
- **Target ($y$):** `fault` (Binary: `0` = Normal, `1` = Fault).
- **Dataset Validation:** Strict schema checks ensure all required columns exist, no missing values are present, and target values are strictly binary (`{0, 1}`).
- **Data Splitting:** 80/20 train-test split stratified on the target `fault` column (`stratify=y`) with a fixed seed (`random_state=42`) for reproducibility.
- **Model Choice:** `DecisionTreeClassifier` trained on `X_train` and evaluated strictly on unseen `X_test`.

## 4. Key Results & Generalization
- **Baseline Accuracy (max_depth=3):** ~95% manual and sklearn score match verified via `assert`.
- **Hyperparameter Tuning (Tree Depth):**
  - **Underfitting:** At `max_depth=1`, the model suffers from high bias (low training & testing accuracy).
  - **Optimal Depth:** `max_depth=3` achieves the best balance between training performance and unseen generalization without excessive variance gap.
  - **Overfitting:** Unconstrained trees (`max_depth=None` or high depth) score near 100% on training data but exhibit a growing gap when tested on unseen data.

## 5. Execution Instructions
Run the main pipeline using `uv` from the course root directory:
```bash
uv run python week09/ml_pipeline.py
```

## 6. Limitations & Responsible Use
- **Data Limitations:** Missing operational contextual metrics such as maintenance history, component age, and ambient environmental humidity.
- **Decision Risks:**
  - *False Positive (FP):* Unnecessary machine shutdown and wasted maintenance labor costs.
  - *False Negative (FN):* Catastrophic mechanical failure leading to worker safety hazards and costly downtime.
- **Security Warning:** Model bundles saved with `joblib` should only be loaded from verified, trusted sources due to arbitrary code execution risks during deserialization.