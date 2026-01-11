# Define a function even_odd() that checks whether a given number is even or odd.

def even_odd(number):
    print(f"{number} is", 'Even Number' if number % 2 == 0 else "Odd number")

even_odd(6)