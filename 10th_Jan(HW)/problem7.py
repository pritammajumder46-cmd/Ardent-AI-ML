# Create a function greet(name) that prints "Good Morning" along with the given name.

def greet(name):
    print(f"Good Morning {name.title()}")

your_name = input("Enter uour first name: ")
greet(your_name)
