# Student Calculation with function
def Calculator (num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num3
    try:
        div = num1 / num2
    except ZeroDivisionError:
        print("Division by Zero not possible")
    return sum, sub, mul, div

