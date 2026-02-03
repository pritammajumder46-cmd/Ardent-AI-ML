# CREATE A FILE WITH YOUR NAME AS THE FILENAME. WRITE A SHORT PARAGRAPH ABOUT YOURSELF IN THE FILE AND WRITE A PROGRAM TO FOUND HOW MANY LINES ARE PRESENT IN THE FILE

import os

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


lines = 0

with open("MySelf.txt", "r") as file:
    for check_lines in paragraph:
        lines += 1 

print(f"\nTotal number of lines in the paragraph is {lines}\n")