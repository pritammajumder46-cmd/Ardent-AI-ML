# Write a program to count the total number of words in a text file

with open("data2.txt", "r") as file:
    paragraph = file.read()

print(f"The Paragraph is: {paragraph}")

words = paragraph.split() #.split() breaks the string into words using spaces by default
print(len(words))