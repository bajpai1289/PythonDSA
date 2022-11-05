def test_location(arr,query,mid):
    midnum=arr[mid]
    if midnum==query:
        if mid-1>=0 and arr[mid-1]==query:
            return 'left'
        else: return 'found'
    elif midnum>query:
        return 'left'
    else: return 'right'

def binary_search(arr,query):
    lo,hi = 0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        result = test_location(arr,query, mid)
        if result == 'found':
            return mid
        elif result=='left':
            hi=mid-1
        elif result == 'right':
            lo=mid+1
    return -1

arr=[i for i in range(10000000)]
query=9999998
print(binary_search(arr,query))


# print(arr.index(query))


