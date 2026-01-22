# Write a program to remove a specific element from a set entered by the user.


flag =0

set1 = {1,2,3,4,5}
print(f"A : {set1}")

del_key = int(input("Enter the value you want to delete from the set: "))

for element in set1:
    if (element == del_key):
        set1.remove(element)
        flag = 1
        break

if flag == 0:
    print(f"{del_key} not fount on the set A")
else:
    print(f"After deleting {del_key} revised set is: {set1}")