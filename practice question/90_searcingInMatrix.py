def searchMatrix(matrix: 'list[list[int]]', target: int) -> bool:
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
    lo=0
    hi = len(matrix)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if matrix[mid][0]<=target and matrix[mid][-1]>=target:
            return search(matrix[mid], target=target)
        elif matrix[mid][0]>target:
            hi=mid-1
        elif matrix[mid][-1]<target:
            lo=mid+1
    return False
    


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 34))
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 32))
print(searchMatrix(matrix = [[1]], target = 1))