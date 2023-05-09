# duplicate cannot be in the solution

nums = [-3,3,4,-3,1,2]
# to brute force iterate over the array twice, but there will be repitition of elemets as 
# there is -3 twice
# step 1: sort the input array
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i> 0 and a == nums[i-1]: # means we are using the same values twice
            continue

        l, r = i+1, len(nums)-1
        while l<r:
            threeSum= a+nums[l]+nums[r]
            if threeSum> 0:
                r-=1
            elif threeSum<0:
                l+=1
            else:
                res.append([a, nums[l], nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    return res
        


print(threeSum(nums))