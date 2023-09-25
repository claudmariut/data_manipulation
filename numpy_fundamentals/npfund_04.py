import numpy as np

array_a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(array_a)

array_b = array_a.reshape(2, 8)
print(array_b)

array_c = array_a.T
print(array_c)

# To print only the two columns in the middle
print(array_c[:, 1:3])

# To print only the two rows in the middle
print(array_c[1:3, :])

# From the second column starting at the end, return the second element in the column
print(array_c[:, -2][1])
