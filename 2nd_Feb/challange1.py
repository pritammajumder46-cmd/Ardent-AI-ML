# Access an index in a list and handle Index error
import os
os.system("cls")

list1 = []

while True:
    try:
        num = int(input("How many number you want to add on the list: "))
        if num > 0:
            break
        else:
            raise ValueError("Non-negative numbers are not allowed")
    except ValueError:
        print("Enter an intiger")

for item in range(1, num+1):
    while True:
        try:
            val = int(input(f"Enter list item number {item}: "))
            list1.append(val)
            break
        except ValueError:
            print("Enter Integers Only")


while True:
    try:
        print(f"\n{list1}")
        key = int(input("\nWhich index's value you want to find on the list: "))
        print(f"the value of index {key} is {list1[key]}")
        break
    except ValueError:
        print("Enter an Intiger Correctly")
    except IndexError:
        print("Index not found, Enter the Intiger Correctly")
    
print("\nAccessing an index with handling the error is done\n")
    