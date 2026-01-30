# Define a function is_zero(n) that checks whether the given number is zero or not.

def is_zero(n):
    print(f"{n} is", "Zero" if n == 0 else "Non Zero")

num = int(input("Enter a number: "))
is_zero(num)