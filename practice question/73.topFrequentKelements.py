from collections import OrderedDict, Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    # d={}
    # for i in nums:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # d=dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    # res=[]
    # count=0
    # return[i for i in d.keys()][:k]
    return list(dict(sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)).keys())[:k]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))

a=4
def k(a):
    a=a+4
k(a)
print(a)


# def over1(a: int, b: int, c:str):
#     print(f"a={type(a)}, b={type(b)}, c is {type(c)}")

# def over1(a: int, b: list):
#     print(f"a={type(a)}, b={type(b)}")


# over1(4,[3,4,5,6],"serd")
se = {1,2,3,4,4,4,4}
print(se[0])