# Define a function find_cube(n) that prints the cube of a given number.

def find_cube(n):
    cube = n ** 3
    return cube

val = float(input("Enter a number: "))
cube1 = find_cube(val)

print(f"cube of {val} is {cube1}")