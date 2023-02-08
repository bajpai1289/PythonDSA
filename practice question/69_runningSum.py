def largestAltitude(gain: list[int]) -> int:
    _sum=0
    newArr=[]
    newArr.append(0)
    for i in gain:
        _sum+=i
        newArr.append(_sum)
    return (newArr)

print(largestAltitude([-4,-3,-2,-1,4,3,2]))