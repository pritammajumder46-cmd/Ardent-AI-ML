# ATM SIMULATION

def withdraw(balance, amount):
    if amount <= balance:
        return balance-amount
    else:
        return "Insufficient Balance"

# import ATM
from ATM import withdraw
balance = 5000
# print(ATM.withdraw(balance,1200))
print(withdraw(balance,1200))