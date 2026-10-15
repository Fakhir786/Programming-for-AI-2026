import numpy as np

# B1 - Create arrays

marks = np.array([78, 85, 91, 66, 88])

matrix = np.arange(12).reshape(3, 4)

images = np.zeros((2, 4, 4))

identity = np.eye(4)

values = np.linspace(0, 1, 10)


# B2 - Inspect every array

print("Marks")
print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Size:", marks.size)
print("Data type:", marks.dtype)
print()

print("Matrix")
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)
print()

print("Images")
print("Shape:", images.shape)
print("Dimensions:", images.ndim)
print("Size:", images.size)
print("Data type:", images.dtype)
print()

print("Identity Matrix")
print("Shape:", identity.shape)
print("Dimensions:", identity.ndim)
print("Size:", identity.size)
print("Data type:", identity.dtype)
print()

print("Values")
print("Shape:", values.shape)
print("Dimensions:", values.ndim)
print("Size:", values.size)
print("Data type:", values.dtype)
print()

# marks.shape is (5,) because it is a one-dimensional array
# containing 5 elements.

# matrix.shape is (3, 4) because it has 3 rows and 4 columns.

print("matrix.size is 12:", matrix.size == 12)
print("images.ndim is 3:", images.ndim == 3)