import numpy as np

# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Basic operations
sum_result = arr1 + arr2
difference_result = arr2 - arr1
product_result = arr1 * arr2
quotient_result = arr2 / arr1

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(matrix1, matrix2)

# Universal functions (ufunc)
square_root = np.sqrt(arr1)
exponential = np.exp(arr1)
logarithm = np.log(arr1)

# Statistics
mean_value = np.mean(arr1)
max_value = np.max(arr1)
min_value = np.min(arr1)
standard_deviation = np.std(arr1)

# Indexing and slicing
subset = arr1[1:4]

# Reshaping
reshaped_arr = arr1.reshape(1, 5)

# Random numbers
random_array = np.random.rand(3, 3)

# Check the shape and data type of an array
shape_of_arr = arr1.shape
data_type_of_arr = arr1.dtype

# Concatenation
concatenated_arr = np.concatenate((arr1, arr2))

# Stacking
stacked_arr = np.vstack((arr1, arr2))

# Boolean indexing
bool_indexing = arr1[arr1 > 2]

# Broadcasting
broadcasted_arr = arr1 + 10

# Save and load NumPy arrays
np.save('saved_array.npy', arr1)
loaded_array = np.load('saved_array.npy')

# Print results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Matrix Product:", matrix_product)
print("Square Root:", square_root)
print("Exponential:", exponential)
print("Logarithm:", logarithm)
print("Mean Value:", mean_value)
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Standard Deviation:", standard_deviation)
print("Subset:", subset)
print("Reshaped Array:", reshaped_arr)
print("Random Array:", random_array)
print("Shape of Array:", shape_of_arr)
print("Data Type of Array:", data_type_of_arr)
print("Concatenated Array:", concatenated_arr)
print("Stacked Array:", stacked_arr)
print("Boolean Indexing:", bool_indexing)
print("Broadcasted Array:", broadcasted_arr)
print("Loaded Array:", loaded_array)
