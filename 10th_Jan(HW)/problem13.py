# Create a function named area_square(side) that calculates and prints the area of a square.

def area_square(side):
    area = side ** 2
    print(f"Area of the square having side of {side} unit is {area:.2f} unit square")

square_side = float(input("Enter a value: "))
area_square(square_side)