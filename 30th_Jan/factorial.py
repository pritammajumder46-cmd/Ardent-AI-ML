import os
os.system("cls")


def Facto(num):
    if num>=1:
        fact = 1
        for i in range (num,0,-1):
            fact *= i
        return fact

    elif num == 0:
        return 1

    else:
        message = "Factorial of -ve number is not possible"
        return message

print("-----------------FACTORIAL CALCULATOR--------------------\n")

number = int(input("Enter a number: "))
factorial_value = Facto(number)
print(f"Factorial of the number is: {factorial_value}\n")

print("-----------------FACTORIAL CHECK DONE--------------------\n\n")