import numpy as np


# ==========================================
# F1 - Incompatible shapes
# ==========================================

# Error:
# The two arrays cannot be added because their shapes are different.

# Cause:
# a has shape (3, 4), while b has shape (3, 2).
# These shapes are not compatible for broadcasting.

# Fix:
# Make b the same shape as a if the intention
# is to add the arrays element by element.


a = np.ones((3, 4))

b = np.ones((3, 2))


# Corrected b

b_fixed = np.ones((3, 4))


result = a + b_fixed


print("F1 - Corrected result:")
print(result)

print()


# ==========================================
# F2 - Array Boolean logic
# ==========================================

# Error:
# NumPy arrays cannot use Python's "and"
# for element-wise comparisons.

# Cause:
# We need to compare every element separately.

# Fix:
# Use & for element-wise AND.
# Put each condition inside parentheses.


values = np.array([10, 20, 30, 40])


selected = values[
    (values > 15)
    &
    (values < 35)
]


print("F2 - Corrected selection:")
print(selected)

print()


# ==========================================
# F3 - Wrong axis
# ==========================================

# Error:
# axis=0 calculates the average of each column.

# Cause:
# Each student is represented by a row.
# We need one average for each row.

# Fix:
# Use axis=1.


scores = np.array([
    [70, 80, 90],
    [60, 75, 85]
])


student_averages = np.mean(
    scores,
    axis=1
)


print("F3 - Corrected student averages:")
print(student_averages)