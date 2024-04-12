import numpy as np

# Creating a vector
v = np.array([1, 2, 3])
print("Vector v:", v)

# Vector operations
# Scalar multiplication
scalar = 2
result = scalar * v
print("Scalar multiplication:", result)

# Dot product
u = np.array([4, 5, 6])
dot_product = np.dot(v, u)
print("Dot product:", dot_product)

# Cross product
cross_product = np.cross(v, u)
print("Cross product:", cross_product)
