import numpy as np

# Define the matrix
matrix = np.array([
    [1, 5],
    [3, 8]
])

# Find the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

print("Original matrix:")
print(matrix)

print("\nInverse matrix:")
print(inverse_matrix)
