from collections import OrderedDict
def topKFrequent(nums: list[int], k: int) -> list[int]:
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d=dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    res=[]
    count=0
    return[i for i in d.keys()][:k]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))