# Prime Numbers: Generate prime numbers between 1 and 50

def isPrime(num):
    flag = 0
    for i in range(2,int((num/2))):
        if num % i == 0:
            flag = 1
            break;
    if(flag == 0):
        return num

prime_list = []

for i in range (2,51):
    if isPrime(i) != None:
        prime_list.append(isPrime(i))

print(prime_list)