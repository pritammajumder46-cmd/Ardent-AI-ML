# TOTAL NUMBER OF ROWS

with open("students.csv", "r") as file:
    rows = file.readlines() # readlines 
print(f"Total rows:",len(rows)-1)

# TOTAL NUMBER OF ROWS
with open("students.csv", "r") as file:
    coulmns = file.readline().strip().split(",")
print(f"Total Coulmns:",len(coulmns))


# DISPLAY THE FIRST FIVE RECORDS OF THE FILE
# import pandas as pd
# print((pd.read_csv("students.csv", index_col="StudentID")).head(5))
with open("students.csv", "r") as file:
    for i in range(6):
        print(file.readline().strip())

# COUNT TOTAL NUMBER OF CHARACTER IN A LINE
char_count = 0
with open("students.csv","r") as file:
    data = file.read()

for letters in data:
    char_count += 1
    # content = file.read()

print(f"{char_count} characters present in the csv file")
# print(f"{len(content)} characters present in the csv file")

# APPEND A NEW STUDENT DATA
StudentID_user = int(input("\nEnter the student id"))
Name_user = input("Enter the name of the student: ")
Age_user = int(input("Enter the age: "))
Gender_user = input("Enter the gender: ")
Course_user = input("Enter the Course: ")
Score_user = input("Enter the score: ")

with open("students.csv", "a") as file:
    file.write(f"{StudentID_user},{Name_user},{Age_user},{Gender_user},{Course_user},{Score_user}")

print("\nNew data Successfully added")

# REPLACE THE COURSE NAME JAVA WITH CORE JAVA
with open("students.csv", "r") as file:
    content = file.read()
content = content.replace('Java','Core Java')

with open("students.csv","w") as file:
    file.write(content)
print("Updated Successfully")

# DELETE THE DATA BY NAME

nametodelete = "Suman"

with open("students.csv","r") as file:
    lines = file.readlines()

with open("students.csv", "w") as file:
    for line in lines:
        if nametodelete not in line:
            file.write(line)

print("Record deleted successfully")

