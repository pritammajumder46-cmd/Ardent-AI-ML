# Remove Duplicates: Remove duplicates while preserving order

l = int(input("Enter how many elemnets you want to enter: "))
list1 = []
non_duplicate_list = []

for i in range(l):
    val = int(input(f"Enter element number {i+1}: "))
    list1.append(val)

for i in list1:
    if i not in non_duplicate_list: # Membership operator is used
        non_duplicate_list.append(i)

print(f"Entered list: {list1}")
print(f"List with non duplicate item: {non_duplicate_list}")

