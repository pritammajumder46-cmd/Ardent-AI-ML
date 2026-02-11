import os
from maths import add,sub

os.system("cls")

a = float(input("Enter 1st Number: "))
b = float(input("Enter 2nd Number: "))

print("\nSummation value is:",add(a,b))
print("Subtraction value is:",sub(a,b))