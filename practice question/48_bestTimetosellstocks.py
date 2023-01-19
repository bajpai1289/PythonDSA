def maxProfit(prices: list[int]) -> int:
    local_profit=0
    global_profit=0
    for i in range(0, len(prices)):
        if len(prices[i+1:])==0:
            return global_profit
        local_max=max(prices[i+1:])
        if prices[i]<local_max:
            local_profit=local_max-prices[i]
        if local_profit>global_profit:
            global_profit=local_profit

    return global_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2]))
print(maxProfit([7,6,4,3,1]))