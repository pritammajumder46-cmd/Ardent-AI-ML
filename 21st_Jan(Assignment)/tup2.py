# Convert a tuple into a list and add a new element to it

tup = (11,22,33,44,55,66,77,88)
print(tup)
l = list(tup)
print(l)
print(type(tup))
print(type(l))

l.append(99)
print(f"After adding a new element the updated list is : {l}")