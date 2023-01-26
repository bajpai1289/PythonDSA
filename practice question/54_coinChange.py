
def coinChange(coins: 'list[int]', amount: int, stack=0, counter=0):
    options=[None]*len(coins)
    if amount <= 0:
        return coins, 0, stack, counter
    if coins and amount:
        for i in range(len(coins)):
            options[i]=coinChange(coins, amount-coins[i], stack+1, counter+1)
    return min(options)


            
        
    

print(coinChange(coins = [1,2,5], amount = 11))
print(coinChange(coins = [2], amount = 3))
print(coinChange(coins = [1], amount = 0))
