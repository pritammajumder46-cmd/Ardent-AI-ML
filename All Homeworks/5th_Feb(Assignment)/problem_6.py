# Write a program to check whether a given word exists in a file or not (case-sensitive).

with open("data.txt", "r") as file:
    pargraph = file.read() 

check = input("\nEnter a word you want to search(Case-sensitive): ")
pargraph = pargraph.split()

flag =0

for words in pargraph:
    if check == words:
        print(f"\"{check}\": this word is present on the paragraph")
        flag = 1
        break

if flag == 0:
    print(f"\"{check}\": This word is not present on the paragraph\n")