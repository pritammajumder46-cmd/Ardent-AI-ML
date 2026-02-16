# Write a program to calculate parking charges for different types of veichles based on duration of parking
# The program should take 2 types of vehicles (2 wheeler or 4 wheeler),
# The number of veichle, and the duration of parking as input
# Then calculate and display the result

class Parkinglot:
    def __init__(self, wheeler_type, number, duration):
        self.wheeler_type = wheeler_type
        self.number = number
        self.duration = duration


class TwoWheeler(Parkinglot):
    def Calculate_Charges(self):
        return 50 * self.number * self.duration


class FourWheeler(Parkinglot):
    def Calculate_Charges(self):
        return 100 * self.number * self.duration


a = int(input("Enter vehicle type [1 for 2 wheeler / 2 for 4 wheeler]: "))

match a:
    case 1:
        nc = int(input("Enter number of vehicles: "))
        nh = int(input("Enter number of hours: "))
        obj = TwoWheeler("2-wheeler", nc, nh)
        print(f"Your Charge is ₹{obj.Calculate_Charges()}")

    case 2:
        nc = int(input("Enter number of vehicles: "))
        nh = int(input("Enter number of hours: "))
        obj = FourWheeler("4-wheeler", nc, nh)
        print(f"Your Charge is ₹{obj.Calculate_Charges()}")

    case _:
        print("Enter a valid value.")
