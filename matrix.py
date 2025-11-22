import numpy as np 


A = np.array([[24, 31],
              [58, 14]])

B = np.array([[11, 23],
              [20, 71]])

print("\n=== MATRIX OPERATIONS ===")

# Dot product
print("\nDot product (A • B):\n", np.dot(A, B))

# Transpose
print("\nTranspose of A:\n", A.T)

# Inverse
if np.linalg.det(A) != 0:
    print("\nInverse of A:\n", np.linalg.inv(A))
else:
    print("\nMatrix A is not invertible.")
