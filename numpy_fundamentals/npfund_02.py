import numpy as np

# 3x3
seq_a = [1, 2, 3]
seq_b = [4, 5, 6]
seq_c = ['7', 8, 9]  # String has the highest order of precedence
seq_d = [10.5, 11, 12]  # Float has higher order than integer

# Array always transforms to higher order of precedence.
array_abc = np.array([seq_a, seq_b, seq_c, seq_d])
print(array_abc)
print(array_abc.shape)


a = [True, True, True]
array_a = np.array(a)
print(array_a)

# Boolean has lower level of precedence than integer. Then F=0 and T=1
b = [False, True, 8]
array_b = np.array(b)
print(array_b)