import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])


# 1. First row
# Expected shape: (4,)

first_row = data[0]

print("First row:")
print(first_row)
print("Shape:", first_row.shape)
print()


# 2. Last column
# Expected shape: (4,)

last_column = data[:, -1]

print("Last column:")
print(last_column)
print("Shape:", last_column.shape)
print()


# 3. Middle 2 x 2 block
# Expected shape: (2, 2)

middle_block = data[1:3, 1:3]

print("Middle 2 x 2 block:")
print(middle_block)
print("Shape:", middle_block.shape)
print()


# 4. Every second row
# Expected shape: (2, 4)

every_second_row = data[::2]

print("Every second row:")
print(every_second_row)
print("Shape:", every_second_row.shape)
print()


# 5. Values greater than 75
# Expected values:
# 80, 90, 100, 110, 120, 130, 140, 150, 160

greater_than_75 = data[data > 75]

print("Values greater than 75:")
print(greater_than_75)
print()


# 6. Values divisible by 20
# Expected values:
# 20, 40, 60, 80, 100, 120, 140, 160

divisible_by_20 = data[data % 20 == 0]

print("Values divisible by 20:")
print(divisible_by_20)
print()


# Example of combined conditions
# Use & instead of "and".
# Each condition must be inside parentheses.

selected = data[(data > 75) & (data < 150)]

print("Values greater than 75 and less than 150:")
print(selected)