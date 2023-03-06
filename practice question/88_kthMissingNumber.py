def findKthPositive(arr: list[int], k: int):
    hi=len(arr)-1
    lo=0
    while lo<=hi:
        mid=(lo+hi)//2
        print('arr[mid]=', arr[mid])
        print('mid=', mid)

        # print(arr[mid]-mid-1)
        if arr[mid]-mid-1<k:
            lo=mid+1
        else:
            hi=mid-1
    return lo+k


print(findKthPositive(arr = [2,3,4,7,11], k = 5))
# print(findKthPositive(arr = [1,2,3,4], k = 2))