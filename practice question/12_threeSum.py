nums = [-1, 0, 1, 2, -1, -4]
output = [[1,0,-1], [2,-1,-1]]

#Brute force solution
# n = len(nums)
# result = []
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             if nums[i]+nums[j]+nums[k]==0:
#                 temp=[nums[i], nums[j], nums[k]]
#                 temp.sort()
#                 result.append(temp)
                
                
# print(result)
                
#using twoSum by fixing an element
n=len(nums)
result = []
for i in range(n-2):
    d={}
    for index, element in enumerate(nums[i+1:]):
        if element in d:
            result.append([i,d[element], index])
        else:
            d[0-element]=index
            
print(result)