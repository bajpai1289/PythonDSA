# given an array of integers in sorted order return last and first index of an element
def locate_first(arr,query):
    def condition(mid):
        if arr[mid]==query:
            if mid>0 and arr[mid-1]==query:
                return 'left'
            else:
                return 'found'
        elif arr[mid]>query:
            return 'left'
        elif arr[mid]<query:
            return 'right'
    return binary_search(0,len(arr)-1,condition)

def binary_search(lo,hi,condition):
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result == 'left':
            hi=mid-1
        elif result == 'right':
            lo=mid+1
    return -1
def locate_last(arr,query):
    def condition(mid):
        if arr[mid]==query:
            if mid<len(arr)-1 and arr[mid+1]==query:
                return 'right'
            else: return 'found'
        elif arr[mid]>query:
            return 'left'
        elif arr[mid]<query:
            return 'right'
    return binary_search(0,len(arr)-1,condition)
# arr=[2,4,6,8,10,12]
q=6


#using my once good working pythoin brain

nums=[0,0,2,2,2,2,2,2,4,4,6,8,8]
arr=[]
target=2
if target in nums:
    arr.append(nums.index(target))
    nums=nums[::-1]

    arr.append(len(nums)-nums.index(target)-1)
    print( arr)
else:
    print([-1,-1])
    
arr=[0,0,2,2,2,2,2,2,4,4,6,8,8]
print(locate_first(arr,target),locate_last(arr,target))
