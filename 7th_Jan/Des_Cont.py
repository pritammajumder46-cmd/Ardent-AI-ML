# 1.wap a code to ckeck if you are eligible for vote or not

age=int(input("Enter your age : "))
if age>=18:
    print("You are eligible.")
else:
    print("You are not eligible.")    

# 2.wap code to find the greatest among 3 numbers 

number1=int(input('Enter first number:'))
number2=int(input('Enter second number:'))
number3=int(input('Enter third number:'))

if number1>number2 and number1>number3:
    print(f"{number1}")
elif number2>number1 and number2>number3:
    print(f"{number2}")
else:
    print(f"{number3}")        