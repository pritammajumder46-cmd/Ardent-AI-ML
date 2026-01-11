# Write a Python function max_two(a, b) that prints the greater of two numbers.

def max_two(a, b):
    return max(a,b)

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

maximum = max_two(num1,num2)
print(f"{maximum} is greater")