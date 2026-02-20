# Sorting in Numpy array
# np.sort()-> Return the sorted copy of array
# np.sort()-> Return the index copy of array
# ndarray.sort()-> Use for inplace sorting

# 1D array
import numpy as np
x = np.array([7,2,3,9,6])
y = np.sort(x)[::-1] # Normal sorting but descending order
print(y)

x = np.array([7,2,3,9,6])
y = np.argsort(x) # Argument Sorting
print(y)

x = np.array([7,2,3,9,6])
x.sort() # Inplace Sorting
print(x)

# 2D ARRAY
y = np.array([
    [12,11,15],
    [21,25,20],
    [18,27,17]
])
y1 = np.sort(y,axis=0) # axis=0 column wise axis=1 row wise sort(by defaut axis=1) 
y2 = np.sort(y)
print(y1)
print(y2)

y = np.array([
    [12,11,15],
    [21,25,20],
    [18,27,17]
])
y1 = np.argsort(y,axis=0) # axis=0 column wise axis=1 row wise sort(by defaut axis=1) 
y2 = np.argsort(y)
print(y1)
print(y2)