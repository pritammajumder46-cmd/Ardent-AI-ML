# Grade according to marks

marks = int(input("Enter a marks between 0 to 100: "))
if 0 <= marks <= 100 :
    if marks > 90 :
        print("A+")
    elif marks > 80 :
        print("A")
    elif marks > 70 :
        print("B+")
    elif marks > 60 :
        print("B")
    elif marks > 50 :
        print("C")
    elif marks > 40 :
        print("D")
    else:
        print("Not promoted")
else:
    print("Enter a valid number")
    