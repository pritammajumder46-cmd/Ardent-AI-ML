import os
import numpy as np

os.system("cls")

arr = np.array([
    [15,16,17],
    [25,26,27],
    [35,36,37],
    [45,46,47]
])
print(arr)

print("\n")
print(arr[1,])

print("\n")
print(arr[1:3,1:3])

print("\n")
print(arr[:,1:3])

print("\n")
print(arr[1:3,1]) # Wrong by me

print("\n")
print(arr[1:3,1:])

# NOT DONE BY ME
print("\n")
print(arr[:,1])
