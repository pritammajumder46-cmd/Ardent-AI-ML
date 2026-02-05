# CREATE A FILE WITH YOUR NAME AND ADD SOME PARAGRAPH ON THAT FILE
# 1. THE RETURN FIRST FIVE CHARACTERS OF THE FILE 
# 2. RETURN TOTAL NUMBER OF LINES ON THAT FILE
# 3. RETURN FIRST TWO LINES OF THE FILE
# 4. RENAME YOUR FILE 

import os
import time
os.system("cls")

# CREATING THE FILE WITH MY NAME AND APPENDING A PARAGRAPH
try:
    with open("Pritam.txt", "x") as file:
        time.sleep(2)
        print("\"Pritam.txt\" created")
except FileExistsError:
    print("\"Pritam.txt\" already exsists. skipping...")
    time.sleep(2)

# WRITING A PARAGRAPH IN IT
with open("Pritam.txt", "w") as file:
    file.write("Wikipedia is a free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and the wiki software MediaWiki.\nFounded by Jimmy Wales and Larry Sanger in 2001, Wikipedia has been hosted since 2003 by the Wikimedia Foundation, an American nonprofit organization funded mainly by donations from readers\nWikipedia is the largest and most-read reference work in history")

# RETURNING FIRST FIVE CHARACTERS OF THE FILE 
with open("Pritam.txt", "r") as file:
    paragraph = file.read()

for characters in paragraph[0:5]:
    print(characters)

# RETURNING TOTAL NUMBER OF LINES ON THAT FILE
with open("Pritam.txt", "r") as file:
    line = file.readlines()
    lines = len(file.readlines())
    # line = file.readlines()

print(f"\n{lines} line(s) present in the file \"Pritam.txt\"")

# RETURNING FIRST TWO LINES OF THAT FILE
print(line[0].strip())
print(line[1].strip())


# RENAME YOUR FILE 
print("\nRenaming the file as \"Misti.txt\"")
time.sleep(2)
os.rename("Pritam.txt", "Misti.txt")
print("File renamed successfully")