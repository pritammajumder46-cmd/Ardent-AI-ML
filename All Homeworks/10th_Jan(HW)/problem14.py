# Define a function simple_interest(p, r, t) to calculate and print simple interest.

def simple_interest(p,r,t):
    I = p*r*t/100
    return I

p1 = float(input("Enter Principle amount: "))
r1 = float(input("Enter rate of Interest: "))
t1 = float(input("Enter time in year: "))

interest = simple_interest(p1,r1,t1)
print(f"Simple Interest amount is {interest}",)