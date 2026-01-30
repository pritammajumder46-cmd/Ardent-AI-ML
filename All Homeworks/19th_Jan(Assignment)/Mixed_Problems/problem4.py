# List Intersection: Find common elements between two lists

num1 = int(input("Enter how many numbers you want add in list number 1: "))

list1 = []
for i in range(1, (num1+1)):
    val = int(input(f"Enter the Value number {i}: "))
    list1.append(val)


num2 = int(input("Enter how many numbers you want add in list number 2: "))
list2 = []
for i in range(1, (num2+1)):
    val = int(input(f"Enter the Value number {i}: "))
    list2.append(val)

print(f"\nList 1 : {list1}")
print(f"List 2 : {list2}")

print("Common part between this two list is", list(set(list1)&set(list2)))