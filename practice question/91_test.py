def search(arr: 'list[int]', target: int):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            lo=mid+1
        elif arr[mid]>target:
            hi=mid-1
    return False
print(search([1,3,4,5,6,7,8],9))