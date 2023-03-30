def reOrderArray(nums: list[int]):
    """It reorders in the way [nums[0], nums[n], nums[1], nums[n-1]...]"""
    lo, hi= 0, len(nums)-1
    tmp= nums.copy()
    nums.clear()
    while lo<hi:
        nums.append(tmp[lo])
        nums.append(tmp[hi])
        lo+=1
        hi-=1
    if len(tmp)%2==1:
        nums.append(tmp[len(tmp)//2])
    return nums


print(reOrderArray([1,2,3,4]))