def maxArea(height: list[int]):
    lo=0
    high = len(height)-1
    globalMax=0
    while lo<=high:
        currMax = (high-lo)*min(height[high], height[lo])
        globalMax=max(currMax, globalMax)
        if height[lo]<=height[high]:
            lo+=1  
        else:
            high-=1

    return globalMax



# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,1]))
print(maxArea(list(range(1,1000000))))