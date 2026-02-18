# SEARCHING SORTING 
# 1D ARRAY
import numpy as np

arr1 = np.array([1,4,3,6,8,9,11,10,23,3,4,2,3,5,3])
ar1 = np.where(arr1 == 3)
print(ar1)

# FOR 2D ARRAY
arr2 = np.array(
    [
        [1,2,3,4],
        [4,3,5,6],
        [1,3,4,5]
    ]
)
ar2 = np.where(arr2 == 4)
print(ar2)

# FOR 3D ARRAY
arr3 = np.array([[[1,2,3,4],[1,2,3,4],[2,3,4,1],[1,2,2,3]]])
print(arr3.shape)
ar3 = np.where(arr3 == 4)
print(ar3)

# SEARCH EVEN ELEMENTS ABD THERE INDEXES
arr4 = np.array(([1,4,3,6,8,9,11,10,23,3,4,2,3,5,3]))
ar4 = np.where(arr4 % 2 == 0) # INDEX
print(ar4)
for i in ar4:
    print(arr4[i]) # ELEMENTS

# SORTING
# 1D ARRAY

array1 = np.array([25,45,63,89,8,1])
print(np.sort(array1))

# 2D ARRAY
array2 = np.array([[12,11,34],[25,10,55],[10,5,13]])
print(array2)
print(np.sort(arr2))

# 3D ARRAY
array3 = np.array([[[5,4,3],[2,4,5],[3,1,6]],[[23,45,12],[12,34,5],[12,45,80]]])
print(array3)
print(np.sort(array3))


