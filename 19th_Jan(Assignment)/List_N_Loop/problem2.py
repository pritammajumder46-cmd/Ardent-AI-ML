# Even Numbers Only: Create a new list containing only even numbers using a loop

num = int(input("Enter how many elemnets you want to enter: "))
list1 = []
even_list = []

for i in range(num):
    val = int(input(f"Enter value number {i+1}: "))
    list1.append(val)

for i in list1:
    if i % 2 == 0:
        even_list.append(i)
        
print(f"\nOriginal list is : {list1}")
print(f"List that contains only even number : {even_list}")