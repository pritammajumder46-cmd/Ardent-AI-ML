def Give_Pass(marks):
    return "Promoted" if marks>=40 else "Not Promoted" 

from Give_Pass import Give_Pass
marks = int(input("Enter your marks out of 100: "))
print(f"Your are {Give_Pass(marks)}")