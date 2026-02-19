# MATRIX COPY AND VIEW

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0]=42
print(arr)
print(x)

# to understand its a copy or base with arr.base
arr = np.array([11,22,33,44,55])
x1 = arr.copy()
y1 = arr.view()
# arr[0]=42
print(arr) 
print(x1) # none mean it is a copy 
print(y1) # it prints original means it is a view

# SHAPE OF MATRIX 2D ARRAY
print("\n")
a = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(a)
print(a.shape)

# Creating array with dimensions using 'ndmin'
arr = np.array([1,2,3,4,5], ndmin = 5)
print("\n")
print(arr)
print("Shape of array is: ", arr.shape)

# Reshape of Matrix
print("\n")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr) # 3d from 1d

a = np.array([1,2,3,4,5,6,7,8])
try:
    newa = a.reshape(3,3)
except ValueError:
    print("Error: Matrix creating is noy possible")

# Converting 1d array with 8 elements
a1 = np.array([1,2,3,4,5,6,7,8])
newa1 = a.reshape(2,2,-1)
print(newa1)