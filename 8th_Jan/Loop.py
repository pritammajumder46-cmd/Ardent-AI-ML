# Print 1 to 10 using for

for i in range(1,11,2):
    print(i)

# Print 1 to 10 using while

i=1
while(i<=10):
    print(i)
    i+=1

# Sum of all numbers between 1 to 10
sum = 0
for i in range(1,11):
    sum+=i
print(f"Sum of 1 to 10 is {sum}")

# Sum of all evn and odd numbers between 1 to 10

Even = Odd = 0

for i in range(1,11):
    if i % 2 == 0:
        Even+=i
    else:
        Odd+=i

print(f" Even sum of 1 to 10 is {Even}")
print(f" Odd sum of 1 to 10 is {Odd}")


