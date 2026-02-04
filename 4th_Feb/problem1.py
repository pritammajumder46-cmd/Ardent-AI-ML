number = input("Enter a number: ")

smallest = int(number[0])
largest = int(number[0])

for digit in number:
    d = int(digit)   # convert character to integer
    
    if d < smallest:
        smallest = d
    
    if d > largest:
        largest = d

print("Largest digit =", largest)
print("Smallest digit =", smallest)
