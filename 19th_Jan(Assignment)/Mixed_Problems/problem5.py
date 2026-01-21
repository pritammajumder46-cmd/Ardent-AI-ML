# Matrix Sum: Calculate sum of all elements in a matrix

m = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

sum = 0
for row in m:
    for elemnet in row:
        sum += elemnet

print(sum)