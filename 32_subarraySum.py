def subarray_sum_bf(arr, target):
    for i in range(len(arr)):
        for j in range(i,len(arr)+1):
            if sum(arr[i:j])==target:
                return (i,j-1)
            
            j+=1
    else:
        return 'no such subarray'
 

"""
TODO:
1. 
"""
arr=[1,2,3,4,5,6,7]
target=13
print(subarray_sum_bf(arr,target))
print('Actual sum', sum(arr[subarray_sum_bf(arr,target)[0] :subarray_sum_bf(arr,target)[1]+1]))

def subarray_sum2(arr, target):
    n=len(arr)
    for i in range(0,n):
        s=0 #running sum
        for j in range(i, n+1):
            if s==target:
                return i,j
            elif s>target:
                break
            if j<n:
                s+=arr[j]
    return None, None
        
def subarray_sum3(arr,target):
    n=len(arr)
    i,j,s=0,0,0
    while i<n and j<n+1:
        if s== target:
            return i,j
        elif s<target:
            if j<n:
                s+=arr[j]
            j+=1
        elif s>target:
            s-=arr[i]
            i+=1
    return None, None 

