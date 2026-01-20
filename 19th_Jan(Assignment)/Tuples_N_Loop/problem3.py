# Common Elements: Find common elements between two tuples

tup1 = (1,2,3,4,5,6,7)
tup2 = (4,5,6,7,8,9,10,11,12,13)

print(tuple(set(tup1)&set(tup2)))