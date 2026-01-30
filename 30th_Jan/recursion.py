# RECURSION
# The function called itself and it must have a base condition
import os
os.system("cls")

def Facto(n):
    if n==0 or n==1 :
        return 1
    elif (n>1):
        return n * Facto(n-1)
    else:
        return "Factorial not possible"

print("-----------------FACTORIAL CALCULATOR--------------------\n")

number = int(input("Enter a number: "))
factorial_value = Facto(number)
print(f"Factorial of the number is: {factorial_value}\n")

print("-----------------FACTORIAL CHECK BY RECURSION IS DONE--------------------\n\n")