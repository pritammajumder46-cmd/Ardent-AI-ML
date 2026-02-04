# display fibonacci series upto 10 terms

def fibo (num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

for i in range(0, 11):
    print(f"Number {i} term of Fibonacci serirs is: {fibo(i)}")