import numpy as np


# Patient data
# Columns:
# Patient ID, Age, Temperature, Heart Rate, Oxygen Saturation

patient_data = np.array([
    [101, 45, 38.5, 100, 92],
    [102, 23, 36.8, 75, 98],
    [103, 67, 39.1, 110, 89],
    [104, 54, 37.0, 80, 96],
    [105, 34, 38.0, 95, 93],
    [106, 72, 36.5, 70, 97]
], dtype=float)


# 1. Display shape, dimensions, size and data type

print("Shape:", patient_data.shape)

print("Dimensions:", patient_data.ndim)

print("Size:", patient_data.size)

print("Data type:", patient_data.dtype)

print()


# 2. Separate patient IDs and clinical features

patient_ids = patient_data[:, 0].astype(int)

clinical_features = patient_data[:, 1:]


print("Patient IDs:")
print(patient_ids)

print()

print("Clinical features:")
print(clinical_features)

print()


# 3. Calculate average age

average_age = np.mean(patient_data[:, 1])


# Mean of every clinical feature

feature_means = np.mean(clinical_features, axis=0)


print("Average age:")
print(average_age)

print()

print("Mean of every clinical feature:")
print(feature_means)

print()


# 4. Select patients older than 60

older_than_60 = patient_data[patient_data[:, 1] > 60]


print("Patients older than 60:")
print(older_than_60)

print()


# Patients hotter than 38 C

hotter_than_38 = patient_data[patient_data[:, 2] > 38]


print("Patients hotter than 38 C:")
print(hotter_than_38)

print()


# Patients below 94% oxygen

below_94_oxygen = patient_data[patient_data[:, 4] < 94]


print("Patients below 94% oxygen:")
print(below_94_oxygen)

print()


# 5. High-risk patients
#
# Temperature > 38
# AND
# Oxygen < 94

high_risk_mask = (
    (patient_data[:, 2] > 38)
    &
    (patient_data[:, 4] < 94)
)


# Get high-risk rows

high_risk_rows = patient_data[high_risk_mask]


# Get high-risk IDs

high_risk_ids = patient_ids[high_risk_mask]


print("High-risk mask:")
print(high_risk_mask)

print()

print("High-risk count:")
print(np.sum(high_risk_mask))

print()

print("High-risk IDs:")
print(high_risk_ids)

print()


# 6. Normalize only clinical features


feature_min = clinical_features.min(axis=0)

feature_max = clinical_features.max(axis=0)

feature_range = feature_max - feature_min


# Protect against division by zero

normalized_features = np.divide(
    clinical_features - feature_min,
    feature_range,
    out=np.zeros_like(clinical_features, dtype=float),
    where=feature_range != 0
)


print("Normalized clinical features:")
print(normalized_features)

print()


# 7. Required tests


# Normalized matrix must be 6 x 4

assert normalized_features.shape == (6, 4)


# Every normalized value must be between 0 and 1

assert np.all(normalized_features >= 0)

assert np.all(normalized_features <= 1)


# Check that original patient_data was not changed

assert np.array_equal(
    patient_data,
    np.array([
        [101, 45, 38.5, 100, 92],
        [102, 23, 36.8, 75, 98],
        [103, 67, 39.1, 110, 89],
        [104, 54, 37.0, 80, 96],
        [105, 34, 38.0, 95, 93],
        [106, 72, 36.5, 70, 97]
    ], dtype=float)
)


# High-risk IDs must be integers

assert np.issubdtype(high_risk_ids.dtype, np.integer)


print("All patient-analysis tests passed.")

print()


# Save patient data as NumPy binary file

np.save(
    "week05/data/patient_data.npy",
    patient_data
)


# Load NumPy file

loaded_npy = np.load(
    "week05/data/patient_data.npy"
)


# Save normalized features as CSV

np.savetxt(
    "week05/output/normalized_features.csv",
    normalized_features,
    delimiter=",",
    fmt="%.4f"
)


# Load CSV

loaded_csv = np.loadtxt(
    "week05/output/normalized_features.csv",
    delimiter=","
)


# Verify NumPy round trip

assert np.array_equal(
    patient_data,
    loaded_npy
)


# CSV was rounded to 4 decimal places,
# so compare rounded original values.

assert np.allclose(
    np.round(normalized_features, 4),
    loaded_csv
)


print("NumPy .npy round trip passed.")

print("CSV round trip passed with np.allclose.")

print()

print("Original patient_data dtype:")
print(patient_data.dtype)

print()

print("Loaded .npy dtype:")
print(loaded_npy.dtype)