# Print all Prime numbers within a given range
def Prime(num):
    flag = 0
    for i in range (2, (num//2)+1):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        return num

print(Prime(6))

print("Enter a range: ")
start = int(input("Enter a starting number greater than or equal to 2: "))
end = int(input("Enter an ending number: "))

l = []

for i in range (start, end+1):
    if Prime(i) is not None:
        l.append(Prime(i))

print(l)