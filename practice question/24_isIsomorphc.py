def isIsomorphic(s: str,t: str):
    memo={}
    if len(s)!=len(t):
        return False
    n=len(s)
    for i in range(n):
        if i==n:
            return True

        if s[i] in memo:
            if memo[s[i]] !=t[i]:
                return False
            else:
                continue
        else:
            memo[s[i]]=t[i] 
    else:
        return True


print(isIsomorphic('badc','baba'))
# meme={
#     "a":1,
#     "b":2,
#     "c": 3
# }

# print(meme["c"])