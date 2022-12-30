nums = [3,2,4]
target = 6
# nums = [2,7,11,15]
# target = 9

#Brute force solution O(n^2)
# n=len(nums)
# for i in range(n-1):
#     for j in range(i+1, n):
#         if nums[i]+nums[j]==target:
#             print([i,j])
#             break
        
# optimal solution
d={}
for index, element in enumerate(nums):
    if element in d:
        print([d[element], index])
        break
    else:
        d[target-element]=index