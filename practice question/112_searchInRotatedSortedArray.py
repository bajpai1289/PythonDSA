def search(nums: list[int], target: int) -> int:
    def bSearch(arr:list[int], tar: int):
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if arr[mid]==tar:
                return mid
            elif arr[mid]>tar:
                hi=mid-1
            elif arr[mid]<tar:
                lo=mid+1
        return -1
    
    def pointOfRotation(nums: list[int]):
        lo=0
        hi=len(nums)-1
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 0
        while(lo<=hi):
            mid=(lo+hi)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            if nums[mid]>nums[len(nums)-1]:
                lo=mid+1
            if nums[mid]<nums[len(nums)-1]:
                hi = mid-1
        return mid
                
    idx1= pointOfRotation(nums)
    # print(nums[idx1])
    if target == nums[idx1]:
        return idx1
    elif target>=nums[idx1] and target<=nums[-1]:
        return bSearch(nums[idx1:], target)
    else:
        return bSearch(nums[:idx1], target)





print(search(nums = [2,4,5,6,7,0,1], target = 4))
# print(search(nums = [4,5,6,7,0,1,2], target = 3))