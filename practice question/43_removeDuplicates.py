def removeDuplicates(nums: list[int]):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k, v in d.items():
        if v>2:
            d[k]=2
    nums.clear()
    for k, v in d.items():
        nums.extend([k]*v)
    return nums
    # return len(nums)



print(removeDuplicates([0,0,1,1,1,1,2,3,3,4]))