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

# def pr(x,y,z):
#     print(f"x={x}, y={y}, z={z}")

# pr(x=3,z=2,y=1)

# def reverse(num: int):
#     count = 0
#     # print(i)
#     while num>0:
#         print(count)
#         digit = num%10
#         count = count*10+digit
#         num//=10
#     return count

# print(reverse(12345))



# class test:
#     name="shiana"
#     def __init__(self, prof= "developer") -> None:
#         self.profile = prof
#         self.staticProfile = self.name

#     def changeProfile(self, strs='Abhishek'):
#         self.name=strs

# obj = test()
# print(obj.profile)  # print developer
# print(obj.staticProfile) #print shiana
# obj.changeProfile()
# print(obj.name) #print Abhisek
# print(obj.staticProfile) #print shiana??
# print(test.name) #print Shiana??
# test.name= "Kirti"
# print(obj.staticProfile)
# obj1 = test("tanya")
# print(obj1.profile)


def fib(x):
    if x==1:
        return 1
    if x==0:
        return 0
    if x==2:
        return 2
    return fib(x-1)+fib(x-2)

n=5
for i in range(9):
    print(fib(i))

def dp(n):
    arr=[0,1]
    for i in range(n-1):
        arr.append(arr[-1]+arr[-2])
    return arr

print(dp(9))