def findSubset(nums: list[int]):
    subsets , curset = [], []
    helper(0,nums, curset, subsets)
    return subsets

def helper(i, nums, curset, subsets):
    if i>=len(nums):
        subsets.append(curset.copy())
        return
    
    #choice to include nums[i]
    curset.append(nums[i])
    helper(i+1, nums, curset, subsets)
    curset.pop()

    #Choice not ot include nums[i]
    helper(i+1, nums, curset, subsets)


print(findSubset([1,2,3,4,5,6,7,8,9,0]))

def subsetsWithDuplicates(nums: list[int]):
    nums.sort()
    subsets, curset = [], []
    helper2(0, nums, curset , subsets)
    return subsets

def helper2(i, nums, curset, subsets):
    if i>=len(nums):
        subsets.append(curset.copy())
        return
    curset.append(nums[i])
    helper2(i+1, nums, curset, subsets)
    curset.pop()

    while i+1<len(nums) and nums[i]==nums[i+1]:
        i+=1
    helper2(i+1, nums, curset, subsets)


print(subsetsWithDuplicates([2,2,3,1])) 