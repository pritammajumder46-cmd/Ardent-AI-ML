# Exception Handling

# SyntaxError
# print("We are student of SVU"

# Run Time Error[ZeroDivisionError]
# x = 10/0
# print(x)

# TypeError
# a = 2
# b = '1'
# print(a+b)

# KeyError
# d = {'Name':'Rima','Subject':'Python'}
# print(d['Age'])

# FilenotfoundError
# open("svu.txt",'r')

#IndexError
# l = [10,20,30,40]
# print(l[5])

# try[which will cause error]--except[which will run when try block throws error]--else[this block is execute when the code has no error]--finally[this is a statement which will run no matter what]

#Exception Handling

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print(f"The Division result is: {result}")
except ValueError:
    print("TypeError: Enter intigers")
except ZeroDivisionError:
    print ("ZeroDivisionError: Division by zero is not allowed")
else:
    print("Done")
finally:
    print(f"This is a code of division")
