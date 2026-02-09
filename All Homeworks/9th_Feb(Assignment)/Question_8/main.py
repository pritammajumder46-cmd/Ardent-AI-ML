import factorial as fact
num = int(input("\nEnter a positive number to check its factorial: "))

try:
    if num>=0:
        print(f"Factorial of the given number is {fact.fact(num)}\n")
    else:
        raise ValueError("Enter a number greater than or equals to 0\m")
except ValueError as e:
    print(f"ValueError:",e)