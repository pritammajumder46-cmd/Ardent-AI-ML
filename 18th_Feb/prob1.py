# CREATE AN NUMPY ARRAY FIND THE ARRAY INDEX AND ARRY ELEMENT WHICH IS DIVISABLE BY 3 AND 5
import numpy as nm

a = nm.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(a)
print(type(a))

check = nm.where((a % 3 == 0) & (a % 5 == 0))
print(check)

for i in check:
    print(a[i])