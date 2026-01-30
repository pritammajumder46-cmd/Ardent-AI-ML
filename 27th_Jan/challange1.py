# Student Calculatior with function

import os
os.system("cls")

def Calculator (num1, num2):
    sum1 = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    try:
        div = num1 / num2
    except ZeroDivisionError:
        div = "Division by Zero not possible"

    return sum1, sub, mul, div

print("------------------CALCULATOR---------------------\n\n")

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

CalC_Sum, CalC_Sub, CalC_Mul, CalC_div = Calculator(num_1,num_2)

print(f"\nAddition Value is : {CalC_Sum}")
print(f"Subtraction Value is : {CalC_Sub}")
print(f"Multiplication Value is : {CalC_Mul:.2f}")
print(f"Division Value is : {CalC_div:.2f}\n")

print("------------------OPERATIONS DONE---------------------\n\n")