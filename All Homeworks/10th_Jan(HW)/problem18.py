# Write a Python function named add_three(a, b, c) that returns the sum of three numbers.

def add_three(a, b, c):
    sum = a + b + c
    print(f"Sum is {sum}")

num1, num2, num3 = map(int, input("Enter three numbers: ").split())
add_three(num1, num2, num3)