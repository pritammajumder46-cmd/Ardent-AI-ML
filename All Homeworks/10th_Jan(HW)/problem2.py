# Write a Python function named display_name() that prints your name.

def display_name():
    name = input("Enter your name: ")
    name = name.title()
    return name

my_name = display_name()
print(f"Your name is {my_name}")