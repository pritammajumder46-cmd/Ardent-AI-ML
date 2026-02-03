# ATM WITHDRAWAL SYSTEM
import os
os.system("cls")

class InsufficientBalanceError(Exception):
    pass

Bal = 0
print("\n----- Welcome to State Bank of India -----")
print("\n------- Which of the following task you want to Perform -------")

while True:
    check = int(input("\n1. Check balance\n2. Withdraw Money\n3. Deposit Money\n4. Exit\n\n[Enter your choice according to the sl number given at the left side]: "))
    match check:
        case 1:
            print(f"\nYour current account balance is ₹ {Bal:.2f}")
        case 2:
            if Bal == 0:
                print("You account has not sufficient balance")
            else:
                try:
                    withdraw = float(input("How much amount you want to withdraw: "))
                    if withdraw > Bal :
                        raise InsufficientBalanceError(f"You account has not sufficient balance to withdraw ₹ {withdraw:.2f}")
                    else:
                        Bal -= withdraw
                        print(f"₹ {withdraw:.2f} is withdrawn")
                except ValueError:
                    print("Enter the amount in rupees correctly")
                except InsufficientBalanceError as e:
                    print("Error: ", e)
        case 3:
            while True:
                try:
                    Deposit = float(input("How much money you want to deposit: "))
                    Bal += Deposit
                    print(f"₹ {Deposit:.2f} is deposited in your Savings Account")
                    break
                except ValueError:
                    print("Enter the amount in rupees correctly")
        case 4:
            break
        case _:
            print("Enter a correct choice")

print(f"Thank you, your final account balance is: ₹{Bal:.2f}")
print(f"Visit Again")