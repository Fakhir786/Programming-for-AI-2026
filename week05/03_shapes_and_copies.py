import numpy as np


# C1 - Observe shared memory

original = np.array([10, 20, 30, 40, 50])

view = original[1:4]

print("Original before changing view:")
print(original)

view[0] = 999

print("View after changing:")
print(view)

print("Original after changing view:")
print(original)

# The view shares memory with original.
# Therefore, changing the view also changes original.


# C2 - Protect the source

independent = original[1:4].copy()

independent[0] = 555

print()
print("Independent copy:")
print(independent)

print("Original after changing copy:")
print(original)

# The copy has separate memory.
# Therefore, changing independent does not change original.


# C3 - Transform shapes

values = np.arange(1, 13)

# Reshape into 3 x 4
reshaped = values.reshape(3, 4)

# Transpose
transposed = reshaped.T

# Flatten
flattened = reshaped.flatten()


# Two 2 x 2 arrays

array1 = np.array([
    [1, 2],
    [3, 4]
])

array2 = np.array([
    [5, 6],
    [7, 8]
])


# Combine vertically
vertical = np.vstack((array1, array2))


# Combine horizontally
horizontal = np.hstack((array1, array2))


# Split np.arange(12) into 3 equal parts

split_parts = np.split(np.arange(12), 3)


# Print shapes

print()
print("Original shape:", values.shape)

print("Reshaped shape:", reshaped.shape)

print("Transposed shape:", transposed.shape)

print("Flattened shape:", flattened.shape)

print("Vertical stack shape:", vertical.shape)

print("Horizontal stack shape:", horizontal.shape)


print("Split shapes:")

for part in split_parts:
    print(part.shape)


# Print results

print()
print("Reshaped:")
print(reshaped)

print()
print("Transposed:")
print(transposed)

print()
print("Flattened:")
print(flattened)

print()
print("Vertical stack:")
print(vertical)

print()
print("Horizontal stack:")
print(horizontal)

print()
print("Split parts:")

for part in split_parts:
    print(part)