# Tuple Conversion: Convert list to tuple and calculate sum

t = (11,22,33,44,55)
print(t)
print(type(t))
l = list(t)
print(l)
print(type(l))

list_sum = sum(l)
print(f"The sum of the tuple after converting into list is : {list_sum} [Obviously same as tuple]")