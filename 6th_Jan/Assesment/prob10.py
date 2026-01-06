print("Salary hike Section")

sal = int((input("Enter your Salary: ")))
exp = int(input("Enter your year of experience: "))

if exp > 5 :
    sal = sal + (sal * (35/100))
    print(f"Your curren salary will be {sal}")
else:
    sal = sal + (sal * (10/100))
    print(f"Your curren salary will be {sal}")