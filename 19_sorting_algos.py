#Bubble sort

# print(bigList)
def bubbleSortWrecursion(nums):
    n=len(nums)
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            bubbleSortWrecursion(nums)
    return nums


def bubbleSortWOrecursion(nums):
    # nums=list(nums)
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums 
 
def insertionSort(nums):
    nums=list(nums)
    for i in range(len(nums)):
        cur=nums.pop(i)
        j=i-1
        while j>=0 and nums[j]>cur:
            j-=1
        nums.insert(j+1, cur)
    return nums  
arr=[4,4,1,2,3,5,7,8,5,4,1,0]
print(insertionSort(arr))

#DIVIDE AND CONQUER ALGORITHMS
#Merge Sort 

def mergeold(left, right):
    result=[]
    i,j=0,0
    for i in range(len(left)+len(right)):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    return result


def merge(nums1, nums2):    
    # List to store the results 
    merged = []

    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):        
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return the final merged array
    return merged + nums1_tail + nums2_tail

def mergeSort(nums):
    if len(nums)<=1:
        return nums
    
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    left_sorted,right_sorted=mergeSort(left),mergeSort(right)
    sorted_nums=merge(left_sorted,right_sorted)
    return sorted_nums
    
    
    
     
left=[1,3,5,7,9]
right=[2,4,6,8,10]
print(merge(left,right))








