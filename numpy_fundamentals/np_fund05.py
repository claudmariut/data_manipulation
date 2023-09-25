import numpy as np

# The dtype argument allows to specify the data type of the array
array_a = np.array([[1,2,3],[4,5,6]], dtype=float)
print(array_a)

# This method creates array of 0s of given shape
array_b = np.zeros((3,3))
print(array_b)

# This method creates array of 1s of given shape
array_c = np.ones((3,3))
print(array_c)

# This method allows to create array of a specific item. First argument is shape, second is the data.
array_d = np.full((3,3), True)
print(array_d)

# Creates random array of integers between first arguments, of shape third argument
array_e = np.random.randint(-50, 50, (3, 3))
print(array_e)

# Created random floats between 0 and 1. Only takes shape as argument.
array_f = np.random.random([3,3])
print(array_f)
