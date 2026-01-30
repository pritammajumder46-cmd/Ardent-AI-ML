# Sum of List: Calculate the sum of all numbers in a list using a for loop

l = int(input("Enter how many elemnets you want to enter: "))
list1=[]

for i in range(l):
    val = int(input(f"Enter value number {i+1}: "))
    list1.append(val)

sum = 0

for i in list1:
    sum = sum + i

print(f"Your list is: {list1}")
print(f"The sum of the element is: {sum}")