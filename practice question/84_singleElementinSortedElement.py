def singleNonDuplicate(nums: list[int]) -> int:
    hi=len(nums)-1
    lo=0
    while lo<=hi:
        mid=(lo+hi)//2
        idx=mid*2
        if idx+1>=len(nums) or nums[idx]!=nums[idx+1]:
            hi=mid-1
            ans=nums[idx]
        else:
            lo=mid+1
    return ans


print(singleNonDuplicate([1,2,2]))
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))