# Write a program to check whether a given key exists in a dictionary or not

flag = 0
Language = {
    'Advanced' : 'Python',
    'Intermidiate' : 'HTML-CSS-JavaScript',
    'Beginner' : 'C#'
}

search = input(("\nEnter the key you want to find: ")).capitalize()

for key, val in Language.items():
    if(search == key):
        print("\nKey found!!!")
        print(f"{key} : {val}\n")
        flag=1
        break

if flag == 0:
    print(f"{search} key Not found\n")