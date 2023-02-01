def largestRectangleArea(heights: list[int]) -> int:
    lo=0
    hi=len(heights)-1
    globMax=0 
    while lo<=hi:
        if min(heights[lo:hi+1])==0:
            lo+=1
        if len(heights[lo:hi+1])==0: break
        currMax=(hi-lo+1)*min(heights[lo:hi+1])
        globMax=max(currMax, globMax)
        lo+=1
        if lo==hi:
            lo=0
            hi-=1
    return globMax

# print(largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
print(largestRectangleArea([0,4]))