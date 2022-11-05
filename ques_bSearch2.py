''' Rotated List: a list is rotated x number of times. Dtermine the minimum number of times  the original list
was be rotated so to obtaion  the givien list. ALL THE NUMBERS ARE UNIQUE'''
arr=[2,3,4,5,1]
original_arr=[1,2,3,4,5]
#result = 3 as it was right shifter 3 times

#this would be my solution to the problem
# temp1=original_arr.index(arr[0])
# print((len(original_arr)-temp1)%len(arr))

# for log(n) time complexity

# def locate_element(arr,q):

#     def condition(mid):
#         if arr[mid]==q:
#             return 'found'
#         elif arr[mid]>q:
#             return 'left'
#         elif arr[mid]<q:
#             return 'right'
#     return bSearch(0,len(arr)-1,condition)

# def bSearch(lo,hi,condition):

#     while lo<=hi:
#         mid=(lo+hi)//2
#         result=condition(mid)
#         if result=='found':
#             return mid
#         elif result=='right':
#             lo=mid+1
#         elif result=='left':
#             hi=mid-1
#     return -1

# temp1=locate_element(original_arr,arr[0])
# print((len(arr)-temp1)%len(arr))

'''This was the wrong answer as the original arrays is not provided here 
hence you need to devise the solution for only the arrays nums given here'''
# nums=[5,6,0,1,2,3,4]
# def find(arr):
#     lo=0
#     hi=len(arr)-1
#     mid=(hi+lo)//2
#     while(lo<=hi):
#         if nums[mid]>nums[mid-1]:
#             return mid
#         elif nums[mid]
# def locate_element(nums,query):
#     def condition(mid):
#         if nums[mid]==query:
#             return 'found'
#         elif nums[mid]>query:
#             return 'left'
#         else:
#             return 'right'
#     return binarySearch(0,len(nums)-1,condition)
# def binarySearch(lo,hi,condition):
#     while(lo<=hi):
#         mid=(lo+hi)//2
#         result=condition(mid)
#         if result=='found':
#             return mid
#         elif result=='left':
#             hi=mid-1
#         elif result =='right':
#             lo=mid+1
#     return mid
                
# nums=[6,7,1,3,5]
# nums=[2,3,4,5,1]
# nums=[4,5,1,2,3]
# nums=[5,1,2,3,4]
# nums=[-1,-4]
nums=[9,4]
#linear search algorith
def count_rotation_linear(nums):
    pos=0
    while(pos<len(nums)):
        if (pos>0 and nums[pos]<nums[pos-1]):
            return pos
        pos+=1
    return 0
print(count_rotation_linear(nums))
# else:
#     print(nums[len(nums)-1])


# query=4
# print(locate_element(nums,query))

# class Solution:
#     def searchInsert(self, nums):
# lo = 0
# hi = len(nums)-1
# while(lo<=hi):
#     mid=(lo+hi)//2
#     if nums[mid]<nums[mid-1]:
#         print( mid)
#         break
#     elif nums[mid]>nums[mid-1] and nums[mid]<nums[0]:
#         lo=mid+1
#     elif nums[mid]>nums[mid-1] and nums[mid]>nums[0]:
#         hi=mid-1
#         # print(hi)
# print(nums[mid],nums[lo],nums[hi])
        # return (nums[mid],nums[lo],nums[hi])
                

# print(Solution().searchInsert(nums))