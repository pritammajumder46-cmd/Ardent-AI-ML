import ATM_Withdrawal as aw
import Wallet_Withdrawal as ww

balance = 5000
w = int(input("How much amount you want to with draw: "))
check = int(input("\nChoose your Withdrawal Method\n------------------------------\n\n1. ATM Withdrawal\n2. Wallet Withdrawal\n\n[Choose according to the serial number]: "))

match check:
    case 1:
        print(f"₹{w} withdrawn, current balance {aw.ATM_Withdrawal(balance,w)}")
    case 2:
        print(f"₹{w} withdrawn, current balance {ww.Wallet_Withdrawal(balance,w)}")
    case _:
        print("Choose a correct serial number")