from collections import Counter
def compress(chars: list[str]) -> int:
    res=[]
    d = dict(Counter(chars))
    for k, v in d.items():
        res.append(k)
        res.append(v)

    while 1 in res:
        res.remove(1)
    for i in range(len(res)):
        if isinstance(res[i], int) and res[i]>9:
            temp=res.pop(i)
            for j in str(temp):
                res.append(j)
    return res
        



print(compress(["a","a","b","b","c","c","c"]))
print(compress(chars = ["a"]))
print(compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c","c","c"]))