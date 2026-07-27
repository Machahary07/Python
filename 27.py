#1. Find the product of the two matrices and store it into a file
import numpy as np
M = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
N = np.array([
    [9,8,7],
    [6,5,4],
    [3,2,1]
])
print("Matrix M:")
print(M)
print()
print("Matrix N:")
print(N)
print()
P = np.dot(M, N)
print("Product of matrices M and N:")
print(P)