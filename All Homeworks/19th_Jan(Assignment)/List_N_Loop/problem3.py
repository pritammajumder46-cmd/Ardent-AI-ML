# List Reversal: Reverse a list without using reverse() or slicing.

l = int(input("Enter how many elemnets you want to enter: "))
list1=[]
reversed_list = []

for i in range(l):
    val = int(input(f"Enter value number {i+1}: "))
    list1.append(val)

for i in range(-1, -(len(list1)+1), -1):
    reversed_list.append(list1[i])

print(f"\nOriginal List: {list1}")
print(f"Reversed List : {reversed_list}")

