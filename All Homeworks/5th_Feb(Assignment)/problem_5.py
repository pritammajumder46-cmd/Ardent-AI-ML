# Write a program to count: 
# • total characters 
# • number of uppercase letters 
# • number of lowercase letters

with open("data.txt", "r") as file:
    paragraph = file.read()

print(f"The Paragraph is: {paragraph}")

Uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lowercase = 'abcdefghijklmonpqrstuvwxyz'

Uppercase_Val = Lowercase_Val = Character = 0
# print(len(Uppercase))

for letters in paragraph:
    if not letters.isspace():
        Character +=1 

    if letters in Uppercase:
        Uppercase_Val += 1

    if letters in Lowercase:
        Lowercase_Val += 1
print(f"Total number of charcter is: {Character}")
print(f"Total number of Character in uppercase is: {Uppercase_Val}")
print(f"Total number of Character in lowerrcase is: {Lowercase_Val}")
