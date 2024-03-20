# Importing NumPy
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

# Basic array operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Array indexing and slicing
print("Element at index 2:", arr[2])
print("Slicing from index 1 to 3:", arr[1:4])

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(matrix)

# Shape and size of the array
print("Shape of the array:", matrix.shape)
print("Size of the array:", matrix.size)

# Reshaping the array
reshaped_matrix = matrix.reshape(1, 9)
print("Reshaped Array:")
print(reshaped_matrix)

# Element-wise operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
sum_result = array1 + array2
print("Element-wise sum:", sum_result)

# Matrix multiplication
product_matrix = np.dot(matrix, reshaped_matrix)
print("Matrix Multiplication:")
print(product_matrix)
