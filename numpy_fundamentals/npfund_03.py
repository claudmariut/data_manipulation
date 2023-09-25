import numpy as np

array_a = np.array([[1, 2, 3],[4, 5, 6]])
print(array_a.shape)
print(array_a.size)

# Reshape method does not overwrite original array, only returns a copy of the new shape.
array_b = array_a.reshape(3, 2)  # New shape need to be on same size as original.
print(array_b)

# Transpose will reshape exchanging #row by #col and grouping elements different than a manual reshape.
array_c = array_a.T
print(array_c)

# Returns of the array
print(array_c[:])
# Returns all rows and columns. THIS IS DIFFERENT THAN PYTHON LIST.
print(array_c[:, :])
# Returns all rows but only column 2 (Only column 2 in other words)
print(array_c[:, 1])
