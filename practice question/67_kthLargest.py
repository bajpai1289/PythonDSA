import heapq

#quick select algorithm:
def findKthLargest(nums: list[int], k: int) -> int:
    k=len(nums)-k  #to mnake this easy for us 
    def quickSelect(l, r):
        pivot, p=nums[r],l
        for i in range(l,r):
            if nums[i]<=pivot:
                nums[p], nums[i]=nums[i], nums[p]
                p+=1
        nums[p], nums[r]=nums[r], nums[p]
        if p>k:
            return quickSelect(l,p-1)
        elif p<k:
            return quickSelect(p+1,r)
        else:
            return nums[p]
    return quickSelect(0,len(nums)-1)





    # for  num in range(1, len(nums)):

print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
