amount = 57
coins = [10,5,2,1]
res = 0
for i in range(0, len(coins)):
    if amount>0:
        c = amount // coins[i]
        res += c
        amount -= c*coins[i]
print(res)