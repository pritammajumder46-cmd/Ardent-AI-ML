# Artificial Inteliigence is a branch of Computer Science which requitred Human Intelligence
# Machine learning is a part of Computer Science which learns from data and find patterns and predict the data acording to it

# Loan Approval

print("\nWelcome to Bandhan Bank Loan Department\n")

# ---------------- Taking The Value of Income ----------------


while True:
    try:
        income = int(input("Enter your Monthly income: "))
        break
    except ValueError:
        print("Enter your income correctly")

# ---------------- Taking The Value of CIBIL SCORE ----------------

while True:
    try:
        cibil_score = int(input("Enter your CIBIL Score: "))
        if 0 <= cibil_score <= 900:
            break
        else:
            print("Invalid CIBIL Score (must be between 0 and 900)")
    
    except ValueError:
        print("Invalid input! Please enter a number.")

# ---------------- OUTPUT PREDICTION ----------------

if cibil_score >= 800:
    if income > 50000 :
        print(f"Loan Approved")
    elif income >= 30000:
        print(f"Loan Aprroved with Conditions")
    else :
        print(f"Contact with Manager for Loan")

elif cibil_score >= 500:
    if income > 50000 :
        print(f"Loan Aprroved with Conditions")
    else:
        print(f"Contact with Manager for Loan")

else:
    print("Loan approval chance is low, Contact with Manager")

# ---------------- AUTO THANK YOU MESSAGE GENERATION ----------------

print("\nThank You\n")