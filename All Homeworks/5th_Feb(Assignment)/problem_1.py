import os
import time
os.system("cls")

# Write a Python program to create a file named data.txt and write the text "Python file handling practice" into it. 
try:
    with open("data.txt", "x") as file:
        time.sleep(2)
        print("\"data.txt\" Created")
except FileExistsError:
    print("\"Data.txt\" already created")

with open("data.txt", "w") as file:
    file.write("Python file handling practice")
                