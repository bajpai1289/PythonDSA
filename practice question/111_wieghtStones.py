stones = [2,2]
def lastStoneWeight(stones: list[int]) -> int:
    while len(stones)>1:
        stones.sort()
        y=stones.pop()
        x=stones.pop()
        if x!=y:
            stones.append(y-x)
    return stones[0] if stones else 0

print(lastStoneWeight(stones))