#find the non empty subarray with the largest sum

# def brute_force(nums:list[int]):
#     maxSum=nums[0]
#     for i in range(len(nums)):
#         currSum=0
#         for j in range(i,len(nums)):
#             currSum+=nums[j]
#             maxSum=max(maxSum, currSum)
#     return maxSum

def Kadanes(arr: list[int]):
    maxSum=arr[0]
    currSum=0
    for n in arr:
        currSum=max(currSum,0)
        currSum+=n
        maxSum=max(maxSum, currSum)
    return maxSum  

def slidingWindow(nums: list[int]):
    maxSum=nums[0]
    curSum=0
    maxL, maxR=0,0  #result pointers
    l=0
    for r in range(len(nums)):
        if curSum<0:
            curSum=0
            l=r  #if the current sum is less than zero we have to reset the left pointer
        curSum+=nums[r]
        if curSum>maxSum:
            maxSum=curSum
            maxL, maxR=[l,r]
    return maxL, maxR




# print(brute_force([4,-1,2,-7,3,4]))
# print(Kadanes([4,-1,2,-7,3,4]))
print(slidingWindow([4,-1,2,-7,3,4]))