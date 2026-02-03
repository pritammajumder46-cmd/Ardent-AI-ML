# FILE READING SYSTM

import os
os.system("cls")

file_name = input("Enter the name of the file [exampl.txt]: ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: {file_name} not found")
except PermissionError:
    print(f"Error: Permission denied of reading file {file_name}")