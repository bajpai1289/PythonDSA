

# def productExceptSelf(nums: list[int]):
#     prefix,n=1,len(nums)
#     res=[]
#     for i in range(0,n):
#         prefix*=nums[i]
#         res.append(prefix)
#     postfix=1
#     for i in range(n, )


# print(productExceptSelf([1,2,3,4]))



n=['flow', 'flower', 'flight']
print(min(n))
res=[]
for i in n:
    count=0
    for c in i:
        count+=ord(c)
    res.append(count)
print(res)
# print(n[res.index(min(res))])

# n=sorted(n)
# print(n)