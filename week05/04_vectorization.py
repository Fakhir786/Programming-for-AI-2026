import numpy as np


# D1 - Vectorized transformations
# Celsius temperatures
temperatures = np.array([20, 25, 30, 35, 40])


# Convert Celsius to Fahrenheit

fahrenheit = temperatures * 9 / 5 + 32


print("Celsius:")
print(temperatures)

print("Fahrenheit:")
print(fahrenheit)

print()


# Marks

marks = np.array([55, 67, 72, 88, 91])


# Add 5 bonus marks
# Maximum mark is 100

adjusted = np.minimum(marks + 5, 100)


print("Original marks:")
print(marks)

print("Adjusted marks:")
print(adjusted)

print()


# Min-max normalization

if marks.max() == marks.min():

    normalized = np.zeros_like(marks, dtype=float)

else:

    normalized = (marks - marks.min()) / (marks.max() - marks.min())


print("Normalized marks:")
print(normalized)

print()


# D2 - Broadcasting


scores = np.array([
    [70, 75, 80],
    [60, 65, 70],
    [85, 90, 95]
])


bonus = np.array([2, 3, 5])


# NumPy broadcasts bonus to every row

adjusted_scores = scores + bonus


print("Scores:")
print(scores)

print()

print("Bonus:")
print(bonus)

print()

print("Adjusted scores:")
print(adjusted_scores)