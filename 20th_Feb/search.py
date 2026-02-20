import numpy as nm

arr = nm.array([1,5,2,6,8,2])
s = nm.where(arr==2)
print(s)

# Printing index of that elemnt which is greater than 6
s = nm.where(arr>6)
print(s)
print(arr[s])

# Printing Even number index and elements
arr1 = nm.array([1,6,2,5,8,7])
s1 = nm.where(arr1%2 == 0)
print(s1)
print(arr1[s1])

# Printing Odd number
arr1 = nm.array([1,6,2,5,8,7])
s1 = nm.where(arr1%2 == 1)
print(s1)
print(arr1[s1])

# Array iterating(searching elements ine by one)\
a = nm.array([1,2,3])
for elements in a:
    print(elements)

print("\n")
arr2 = nm.array([
    [1,2,3],
    [4,5,6]
])

for row in arr2:
    for column in row:
        print(column)
print("\n")
arr = nm.array(
    [
        [
            [1,2],
            [3,4],
            [5,6],
            [7,8]
        ]
    ]
)
for elements in nm.nditer(arr):
    print(elements)

print("\n")
for elements in nm.ndenumerate(arr):
    print(elements)

# Baisc Operations
a = nm.array([1,2,3])
print("\n")
print(a)
print(a+10)
print(a*2)
print(pow(a,2))
l = len(a)
print(l)

# Joining
# 1D Array
a = nm.array([1,2,3])
b = nm.array([4,5,6])
arr_join = nm.concatenate((a,b))
print(arr_join)
# 2D Array
arr1 = nm.array(
    [
        [1,2],
        [3,4]
    ]
)
arr2 = nm.array(
    [
        [5,6],
        [7,8]
    ]
)

arrr1 = nm.concatenate((arr1,arr2),axis=1)
arrr2 = nm.concatenate((arr1,arr2),axis=0)
print(arrr1)
print(arrr2)

# split
arr = nm.array([1,2,3,4,5,6])
new1 = nm.array_split(arr,4)
new2 = nm.array_split(arr,3)
print(new1[0])
print(new1[1])
print(new1[2])
print(new2)

# Filtering
d = nm.array([10,5,20,3,15])
filterd = d[d>10]
print(filterd)