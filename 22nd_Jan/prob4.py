# Write a program to count how many times a given element appears in a list

l = [1,1,2,2,3,3,3,1,1,1,2,2,3,3,3,4,4,4,1,1,2,2,4,4,4,3]
print(l)

count = 0
key =int(input("Enter the element you want to count at the lsit: "))

for element in l:
    if(element == key):
        count += 1

print(f"{key} is present {count} times in the list")