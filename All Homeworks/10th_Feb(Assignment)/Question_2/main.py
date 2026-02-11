from shapes import circle,square

check = int(input("1. Press 1 for checking the area of a circle\n2. Press 2 for checking the area of a square\n"))
match check:
    case 1:
        r = float(input("Enter a radius: "))
        area1 = circle(r)
        print(f"Area: {area1} square unit")
    case 2:
        s = float(input("Enter a side: "))
        area2 = square(s)
        print(f"Area: {area2} square unit")
    case _:
        print("Choose a valid input")
