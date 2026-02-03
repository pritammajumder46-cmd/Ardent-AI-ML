# STUDENT MARKS LOOKUP

import os
os.system("cls")
class MarksError(Exception):
    pass

print("Welcome to Mathematics Examination marks Software")

while True:
    try:
        num = int(input("Enter how many student's marks you want to add on: "))
        break
    except ValueError:
        print("Enter an Integer Quantity")

marks_list = []

for roll in range(1, num+1):
    while True:
        try:
            val = int(input(f"Enter the marks of roll number {roll}: "))
            if 0 <= val <= 100:
                marks_list.append(val)
                break
            else:
                raise MarksError("Marks should be under 100")
        except ValueError:
            print("Enter a value properly")
        except MarksError as e:
            print("Error: ", e)

print(marks_list)


while True:
    try:
        key = int(input("Enter the roll number of the student to know his/her marks: "))
        print(f"Mathematics marks of roll number {key} is : {marks_list[key-1]}")
        break
    except IndexError:
        print("Enter the Roll number correctly")
