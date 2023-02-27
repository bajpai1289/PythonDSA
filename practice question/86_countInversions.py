count=0
    
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid =len(arr)//2
    left= arr[:mid]
    right= arr[mid:]
    left_sorted, right_sorted=mergeSort(left), mergeSort(right)
    sorted_nums=merge(left_sorted, right_sorted)
    return sorted_nums

    

def merge(arr1:list[int], arr2:list[int]):
    res=[]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    arr1_tail=arr1[i:]
    arr2_tail=arr2[j:]
    return res+arr1_tail+arr2_tail




list1=[2, 3, 4, 5, 6]
arr=mergeSort(list1)
print(arr)

    

