import os
os.system("cls")

def sum_natural(n):
    sum_all = (n*(n+1))/2 # I DIRECTLY USED THE FORMULA
    return sum_all

val = 10
print(f"Sum of all natural numbers till {val} is: {sum_natural(val):.0f}")