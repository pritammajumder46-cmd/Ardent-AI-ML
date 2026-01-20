# Multiplication Table: Print table of a number using nested loops

num = int(input("Enter the number whose multiplication table is to be displayed: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")