def isIsomorphic(s: str,t: str):
    memo1={}
    memo2={}
    if len(s)!=len(t):
        return False

    if len(s)==1:
        return s==t
    n=len(s)
    for i in range(n):
        if s[i] in memo1:
            memo1[s[i]].add(t[i])
        else:
            memo1[s[i]]=set([t[i]])
    for i in range(n):
        if t[i] in memo2:
            memo2[t[i]].add(s[i])
        else:
            memo2[t[i]]=set([s[i]])

    flag1=  all(len(set(i))==1 for i in memo1.values())
    flag2=  all(len(set(i))==1 for i in memo2.values())
    return flag1 and flag2



print(isIsomorphic('badc','baba'))
print(isIsomorphic(s = "egg", t = "add"))
print(isIsomorphic(s = "foo", t = "bar"))
print(isIsomorphic(s = "a", t = "a"))
print(isIsomorphic(s = "ab", t = "ab"))
print(isIsomorphic(s = "ab", t = "aa"))

# meme={
#     "a":1,
#     "b":2,
#     "c": 3
# }

# print(meme["c"])