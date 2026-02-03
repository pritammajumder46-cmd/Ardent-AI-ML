# FILE HANDLING
# ------------------------------
# "x" -> CREATE
# "r" -> READ
# "a" -> APPEND
# "w" -> WRITE
# -------------------------------

# CREATE A FILE
# with open ("svu.txt", "x")as file:
#     print("file created")

# WRITE OPERATION
with open("svu.txt", "w")as file:
    file.write("We are students of B. Tech.")

# SHOW WHAT IS WRITTEN ON THE FILE BY .read() METHID
with open("svu.txt", "r")as file:
    print(file.read())

# APPEND A FILE
with open("svu.txt", "a")as file:
    file.write("\nI love python.")

with open("svu.txt", "r")as file:
    print(file.read())

# with open("su.txt", "w")as file:
#     file.write("abcdefghijklmnopqrstuvwxyz")


# RENAME A FILE
import os
# os.rename("su.txt","abcd.txt")

# RENAME A FILE
os.remove("abcd.txt")