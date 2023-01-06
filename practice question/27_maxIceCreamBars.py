def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    if coins<costs[0]:
        return 0
    i=0
    sum=0
    while i<len(costs) and sum<coins:
        sum+=costs[i]
        i+=1
    return i,sum


print('Test case 1:')
try:
    print(maxIceCream(costs =[1,3,2,4,1], coins = 319353))
except Exception as e:
    print(e)


print('Test case 2:')
try:
    print(maxIceCream(costs = [10,6,8,7,7,8], coins = 5))
except Exception as e:
    print(e)


print('Test case 3:')
try:
    print(maxIceCream(costs = [1,6,3,1,2,5], coins = 20))
except Exception as e:
    print(e)


print('Test case 4:')
try:
    print(maxIceCream(costs =[1,3,2,4,1], coins = 7))
except Exception as e:
    print(e)

print('Test case 5:')
try:
    print(maxIceCream(costs =[7,3,3,6,6,6,10,5,9,2], coins = 56)) #expected 9
except Exception as e:
    print(e)