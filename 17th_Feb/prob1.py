# create a 1d numpy array from the list [1,2,3,4,5]. Print the array and its shape

import numpy as np

l = [1,2,3,4,5]
print(l)
print(type(l))

l_array = np.array(l)
print(l_array)
print(type(l_array))
print(l_array.shape)