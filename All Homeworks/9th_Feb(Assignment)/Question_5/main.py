import calculator as calC

a = float(input("\nEnter a number: "))
b = float(input("Enter another number: "))

sum_val = calC.add(a,b)
sub_val = calC.subtract(a,b)
mul_val = calC.multiply(a,b)
div_val = calC.divide(a,b)

print(f"\nResult\n---------------\n\nAddition : {sum_val}\nSubtraction : {sub_val}\nMultipliation : {mul_val}\nDivision: {div_val}\n")