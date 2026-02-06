# Write a program to read and display the entire contents of data.txt.
with open("data.txt", "r") as file:
    paragraph = file.read()

print(paragraph)  