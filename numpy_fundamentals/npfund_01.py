import numpy as np  # This is the standard way to import numpy module

# Numpy arrays are homogeneous
array_a = np.array([1,2,3,4,5])  # Operations using numpy array are much faster than std python lists.
print(array_a)

# Python built-in list are heterogeneous arrays
print([1,2,3,4,5])

# Numpy arrays are dimensional. This operation returns tuple with #rows and #columns
print(array_a.shape)

# Two dimensional array of size 5
array_b = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])

print(array_b)
print(array_b.shape)

# Returns #rows * #cols
print(array_b.size)

