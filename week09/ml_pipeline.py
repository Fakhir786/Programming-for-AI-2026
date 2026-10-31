from pathlib import Path
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# setting up absolute paths as per machine layout
DATA_PATH = Path("F:/FAKHIR/Programming/PFAI/Programming-for-AI-2026/week09/data/machines_ml.csv")
MODEL_PATH = Path("F:/FAKHIR/Programming/PFAI/Programming-for-AI-2026/week09/models/machine_predictor.joblib")
REPORT_PATH = Path("F:/FAKHIR/Programming/PFAI/Programming-for-AI-2026/week09/reports/model_comparison.csv")

# make sure output folders actually exist before saving stuff
Path("week09/models").mkdir(parents=True, exist_ok=True)
Path("week09/reports").mkdir(parents=True, exist_ok=True)

# make sure the dataset is actually there before loading
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset missing at {DATA_PATH}. Place machines_ml.csv in week09/data/")

# load csv and check required columns
machines = pd.read_csv(DATA_PATH)
required = {"temp_c", "vibration", "runtime", "pressure", "fault"}

missing = required - set(machines.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")

# check for any unexpected nulls in required fields
if machines[list(required)].isna().any().any():
    raise ValueError("Required columns contain missing values.")

# ensure target labels are strictly binary (0 or 1)
if not set(machines["fault"].unique()).issubset({0, 1}):
    raise ValueError("fault must contain only 0 and 1.")

# separate features from target class
FEATURES = ["temp_c", "vibration", "runtime", "pressure"]
X = machines[FEATURES]
y = machines["fault"]

# 80-20 stratified split for balanced class proportions
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# initialize and train baseline decision tree classifier
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

# evaluate performance and compute confusion matrix values manually
cm = confusion_matrix(y_test, predictions)
tn, fp, fn, tp = cm.ravel()
manual_accuracy = (tn + tp) / cm.sum()
test_accuracy = accuracy_score(y_test, predictions)

print({"TN": tn, "FP": fp, "FN": fn, "TP": tp})
assert abs(manual_accuracy - test_accuracy) < 1e-12

# plot and save confusion matrix figure
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Normal', 'Fault'])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.savefig(Path("week09/reports/confusion_matrix.png"))
plt.close()

# test different max depths to compare training vs testing accuracy
results = []
for depth in [1, 2, 3, 5, None]:
    candidate = DecisionTreeClassifier(max_depth=depth, random_state=42)
    candidate.fit(x_train, y_train)
    train_score = candidate.score(x_train, y_train)
    test_score = candidate.score(x_test, y_test)
    results.append({
        "max_depth": str(depth),
        "train_accuracy": train_score,
        "test_accuracy": test_score,
        "gap": train_score - test_score
    })

# save comparison table to csv report
comparison = pd.DataFrame(results)
comparison.to_csv(REPORT_PATH, index=False)
print(comparison)

# bundle the trained model and feature list together using joblib
bundle_path = MODEL_PATH
bundle = {
    "model": model,
    "features": FEATURES
}
joblib.dump(bundle, bundle_path)

# reload model bundle to verify integrity and exact output match
loaded = joblib.load(bundle_path)
reloaded_predictions = loaded["model"].predict(x_test[loaded["features"]])
assert (reloaded_predictions == predictions).all()
print("Model reloaded successfully and verified.")

# run predictions on brand new hypothetical machine records
new_machines = pd.DataFrame([
    {"temp_c": 98, "vibration": 6.5, "runtime": 14200, "pressure": 3.2},
    {"temp_c": 61, "vibration": 1.2, "runtime": 2700, "pressure": 6.7},
    {"temp_c": 81, "vibration": 3.8, "runtime": 8600, "pressure": 4.8},
])

# ensure new records match training schema before predicting
feature_order = loaded["features"]
if set(new_machines.columns) != set(feature_order):
    raise ValueError("Prediction columns do not match training features.")

new_machines["predicted_fault"] = loaded["model"].predict(new_machines[feature_order])
print(new_machines)