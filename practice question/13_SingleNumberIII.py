nums=[1,1,2,3,3,4,5,5,5]
# d={}
# result =[]
# for i in nums:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for num, count in d.items():
#     if count==1:
#         result.append(num)
# print(result)

def genNum(nums: list):
    for i in set(nums):
        if nums.count(i)==1:
            yield(i)
            
print(list(genNum(nums)))