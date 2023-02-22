#find the length of the longest subarray, with the same value in each position 
def longestSubarray(nums):
    length=0
    l=0
    for r in range(len(nums)):
        if nums[l]!=nums[r]: l=r
        length=max(length, r-l+1)
    return length
                   
print(longestSubarray([4,2,2,3,3,3]))

'find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values positive'
nums=[2,3,1,2,4,3]
target=6
#brute force solution: go through every single subarray and find all of the subarrays that total upto 6 and then among 
#those subarrays keep track of the lenght of the subarrays