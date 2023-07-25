def peakIndexInMountainArray(arr: list[int]) -> int:
    lo = 0
    hi = len(arr)-1
    while lo<=hi:
        mid = lo+ (hi-lo)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid+1]>arr[mid]:
            lo=mid+1
        elif arr[mid-1]>arr[mid]:
            hi = mid-1
    return lo




print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([2,1,1]))
print(peakIndexInMountainArray([0,2,3,4,8,10, 13, 5,2,1]))