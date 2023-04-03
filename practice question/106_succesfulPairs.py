# def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
#     res=[]
#     for i in spells:
#         res.append(list(map(lambda x:x*i, potions)))
#     for i in range(len(res)):
#         res[i]=list(filter(lambda x:x>=success, res[i]))
#     return [len(i) for i in res]

# print(successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))
# print(successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16))


# sett = ((i for i in range(2,10)))
# print(type(sett))


arr=[[3,2,1],[6,5,4],[9,8,7]]
arr2=[[*i]  for i in arr]
arr2[1].sort()
print(arr)