# Combination by Function
import os
os.system("cls")


def Facto(n):
    if n==0 or n==1 :
        return 1
    else:
        return n * Facto(n-1)

print("-----------------COMBINATION CALCULATOR--------------------\n")

n = int(input("Enter a number: "))
r = int(input("Enter a number less than or equal to previos number: "))

permutation = Facto(n)//(Facto(r)*Facto(n-r))

print(f"{n}C{r} value is {permutation}\n")

print("-----------------COMBINATION CALCULATION DONE--------------------\n")