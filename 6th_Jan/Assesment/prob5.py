# discount

amount= int(input("Enter your bill amount: "))
if amount >= 1000:
    print(f"You got 20% discount")
    discount = amount * (20 / 100)
    amount -= discount
    amount = int(amount)
    print(f"Pay {amount}")
else:
    print(f"No discount.\nPay {amount}")