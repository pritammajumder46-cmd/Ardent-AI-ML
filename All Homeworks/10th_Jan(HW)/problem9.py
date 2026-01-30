# Write a function named multiply() that multiplies two numbers entered by the user.

def multiply(num1, num2):
    mul = num1*num2
    return mul

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

multiplication = multiply(a,b)
print(f"Multiplication of {a} and {b} is {multiplication}")