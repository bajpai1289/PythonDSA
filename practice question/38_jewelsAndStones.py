def numJewelsInStones( jewels: str, stones: str):
    sum=0
    for i in jewels:
        sum+=stones.count(i)

    return sum









print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))

print((['lucy love leetcode'.strip()]))