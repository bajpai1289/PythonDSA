# def searchMatrix(matrix: 'list[int]', target: int):
#     def search(arr: 'list[int]', target: int):
#         lo=0
#         hi=len(arr)-1
#         while lo<=hi:
#             mid=(lo+hi)//2
#             if arr[mid]==target:
#                 return True
#             elif arr[mid]>target:
#                 hi=mid-1
#             elif arr[mid]<target:
#                 lo=mid+1
#         return False
#     lo=0
#     hi=len(matrix)-1
#     while lo<=hi:
#         mid=(lo+hi)//2
#         # print('help step bro im stuck')
#         if matrix[mid][0]<=target and matrix[mid][-1]>=target:
#             return search(matrix[mid], target = target)
#         elif matrix[mid][0]>target:
#             hi=mid-1
#         elif matrix[mid][-1]<target:
#             lo=mid+1
#     return False





# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 34))
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 32))
# print(searchMatrix(matrix = [[1]], target = 1))



# def create(n:int, arr:list=[]):
#     if n<0:
#         return arr
#     arr.append(n)
#     return create(n-1, arr)

# print(create(5))
# var = [1,2,3,4]

# def fn():
#     temp=var[0]
#     var[0]=var[-1]
#     var[-1]=temp
# fn()
# print(var)
# # print(temp)


# arr=[[3,2,1],[6,5,4],[9,8,7]]
# tmp=arr.copy()
# tmp[0].sort()
# print(arr)

def pr(x,y,z):
    print(f"x={x}, y={y}, z={z}")

pr(x=3,z=2,y=1)