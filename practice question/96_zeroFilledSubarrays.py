def zeroFilledSubarray(nums: list[int]):
    counts =[0]
    for i in nums:
        if i==0:
            counts.append(counts[-1]+1)
        else:
            counts.append(0)
    return sum(counts)


print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(zeroFilledSubarray([0,0,0,2,0,0]))