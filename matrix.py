# Define a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix
for row in matrix:
    print(row)

# Accessing elements in the matrix
print("Element at row 2, column 3:", matrix[1][2])  # This prints '6'

# Performing operations on matrices
# For example, let's transpose the matrix
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Print the transposed matrix
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
