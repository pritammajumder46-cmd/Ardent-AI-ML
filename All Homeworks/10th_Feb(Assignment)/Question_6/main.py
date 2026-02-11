from finance.tax import tax
from hr.salary import salary

s = int(input("Enter your Yearly Salary: "))
t = int(input("Enter your yearly tax deduction: "))

in_hand = salary(s) - tax(t)
print(f"Your in hand salary is : ₹{in_hand}")