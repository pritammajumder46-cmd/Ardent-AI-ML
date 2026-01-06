# Find the largest between 2 numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 < num2 :
    print(f"{num2} is greater")
elif num2 < num1 :
    print(f"{num1} is greater")
else:
    print("Both numbers are same")
