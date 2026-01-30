# Fibonacci Sequence: Generate first 10 Fibonacci numbers
def febo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return febo(num-1) + febo(num-2)

fibo_list = []

for i in range(11):
    fibo_list.append(febo(i))

print(f"First 10 fibonacci list is : {fibo_list}")