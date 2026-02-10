def Wallet_Withdrawal(Balance, Withdrawal):
    if Balance - Withdrawal <= 5000:
        return Balance - Withdrawal - 10
    else:
        return Balance - Withdrawal