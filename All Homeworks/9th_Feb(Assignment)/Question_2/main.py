import area
check = int(input("\nArea Calculator\n-----------------------------\n1. Find area of a circle\n2. Find area of a rectangle\n\n[Enter your choice according to sl number]: "))

match check:
    case 1:
        rad = float(input("\nEnter the radious: "))
        area1 = area.circle_area(rad)
        print(f"The area of the circle is {area1:.2f} unit square\n")
    case 2:
        l = float(input("\nEnter the length of the rectangle: "))
        b = float(input("Enter the breadth of the rectangle: "))
        area2 =  area.rectangle_area(l,b)
        print(f"The area of the rectangle is {area2:.2f} unit square\n")
    case _:
        print("Enter a valid input\n")