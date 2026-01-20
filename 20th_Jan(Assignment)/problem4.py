# Check whether one set is a subset of another

flag = 0

num1 = int(input("Enter number of elements in set A: "))
set1 = set()

for i in range(1, num1+1):
    val = int(input(f"Enter value number {i}:" ))
    set1.add(val)

num2 = int(input("Enter number of elements in set B: "))
set2 = set()

for i in range(1, num2+1):
    val = int(input(f"Enter value number {i}:" ))
    set2.add(val)

for i in set2:
    if i in set1:
        continue
    else:
        print("B is not a subset of A")
        flag = 1
        break

if flag == 0:
    print("B is a subset of A")

