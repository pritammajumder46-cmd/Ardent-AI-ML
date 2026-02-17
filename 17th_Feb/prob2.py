# create a matrix from list[[1,2,3],[4,5,6]]. Print the array and its shape

import numpy as np

l = [[1,2,3],[4,5,6]]
print(l)
print(type(l))

l_array = np.array(l)
print(l_array)
print(type(l_array))
print(l_array.shape)