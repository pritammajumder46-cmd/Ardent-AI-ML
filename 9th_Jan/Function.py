#  Sum Function 
def sum(v1, v2):
    ans = v1 + v2
    return ans

a = sum(10, 20)
print(a)


#  Subtraction Function 
def subtraction(v1, v2):
    ans = v1 - v2
    return ans

b = subtraction(10, 20)
print(b)


#  Multiplication Function 
def multiplication(v1, v2):
    ans = v1 * v2
    return ans

c = multiplication(10, 20)
print(c)


#  Division Function 
def division(v1, v2):
    ans = v1 / v2
    return ans

d = division(10, 20)
print(d)


#  Even Number Check 
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

ans = even(2)
print(ans)


# ----------- Odd Number Check
def odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

ans = odd(10)
print(ans)


# Swap Two Numbers Using Function 
def fun(a, b):
    a, b = b, a   # swapping
    return a, b

a = int(input("Enter the a: "))
b = int(input("Enter the b: "))

a, b = fun(a, b)

print(a)
print(b)
