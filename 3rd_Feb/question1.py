# CREATE A FILE WITH YOUR NAME AS THE FILENAME. WRITE A SHORT PARAGRAPH ABOUT YOURSELF IN THE FILE AND WRITE A PROGRAM TO FOUND HOW MANY VOWELS ARE PRESENT IN THE FILE

import os
import time

os.system("cls")
try:
    with open("MySelf.txt", "x") as file:
        print("file created\n")
except FileExistsError:
    print("File Already exsists. So skipping.......\n")


with open("Myself.txt", "w") as file:
    file.write("Hi, I am Pritam. I am a good boy who loves learning and coding. I like to play guitar, study hard, and dream big for my future. I am from West Bengal and I speak Bengali and English. I want to go to IIT and become a smart engineer. I am friendly, funny, and I like to make people smile. I always try my best like a cute baby student")

with open("MySelf.txt", "r") as file:
    paragraph = file.read()
    print(paragraph)


vowel = 0
vowelletters = "AEIOUaeiou"

for letter in paragraph:
    if vowelletters in paragraph:
        vowel += 1 

print(f"\nTotal number of vowels in the paragraph is {vowel}\n")