'''
Given an array return True if there are two elements within a window of size two that are equal
'''
#brute force solution O(n*K)
def closeDuplicatesBF(nums:list[int], k:int):
    for l in range(len(nums)):  #desctibes the beginning of the window
        for r in range(l+1, min(len(nums), l+k)): #right pointer should not be at the same position as l, so initializing at l+1,
            if nums[l]==nums[k]:
                return True
    return False

#to optimise this we can use rollingset() to check for duplicates
def closeDuplicates(nums, k):
    window=set()
    l=0
    for r in range(len(nums)):
        if r-l+1>k:
            window.remove(nums[l])
            l+=1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False

