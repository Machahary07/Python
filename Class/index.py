import numpy as np

# -------------------------------
# 1. Creating Arrays
# -------------------------------
a = np.array([1, 2, 3])                # 1D
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D
z = np.zeros((2, 3))                   # 2x3 zero matrix
o = np.ones((3, 3))                    # 3x3 ones
r = np.random.randint(1, 10, (2, 3))   # random 2x3

# -------------------------------
# 2. Array Info
# -------------------------------
print("Shape:", b.shape)               # rows, columns
print("Size:", b.size)                 # total elements
print("Dimensions:", b.ndim)           # 1D, 2D, 3D

# -------------------------------
# 3. Indexing & Slicing
# -------------------------------
print(b[0, 1])          # element at row0 col1 = 2
print(b[:, 1])          # entire column 1
print(b[1, :])          # entire row 1

# -------------------------------
# 4. Mathematical Operations (element-wise)
# -------------------------------
print(a + 2)            # add 2 to all elements
print(a * 3)            # multiply each element
print(a ** 2)           # power
print(a + b[0])         # broadcasting

# -------------------------------
# 5. Matrix Operations
# -------------------------------
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", m1 + m2)
print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose:\n", m1.T)
print("Inverse:\n", np.linalg.inv(m1))

# -------------------------------
# 6. Aggregate Functions
# -------------------------------
print("Sum:", b.sum())
print("Row-wise sum:", b.sum(axis=1))
print("Column-wise max:", b.max(axis=0))
print("Mean:", b.mean())
print("Std Dev:", b.std())

# -------------------------------
# 7. Reshaping
# -------------------------------
c = np.arange(1, 10)              # 1 to 9
d = c.reshape((3, 3))             # reshape to 3x3
print(d)

# -------------------------------
# 8. Stacking
# -------------------------------
h = np.hstack((a, a))             # horizontal stack
v = np.vstack((a, a))             # vertical stack
print(h)
print(v)

# -------------------------------
# 9. Filtering (Boolean Indexing)
# -------------------------------
print(c[c > 5])      # prints elements >5
