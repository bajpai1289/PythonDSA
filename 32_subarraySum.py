def subarray_sum_bf(arr, target):
    i=0
    j=i
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i:j]==target:
                return (i,j)
            else:
                j+=1
 

"""
1. 
"""