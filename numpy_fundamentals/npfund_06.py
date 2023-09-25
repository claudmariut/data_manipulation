import numpy as np

# The third number will cause an overflow.
array_a = np.array([32766, 32767, 32768], dtype=np.int16)
# To print data type of a numpy array
print(array_a.dtype)

# This will lead to an overflow because the data type is unsigned
array_b = np.array([[-1, 0, 1]], dtype=np.uint16)
print(array_b)
