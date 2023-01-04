def isSubsequence(s:str, t:str):
    t=iter(t); return all(c in t for c in s)
    # count=0
    # idx=0
    # i=0
    # while idx<(len(t)):
    #     while i<len(s):
    #         if s[i]==t[i]:
    #             count+=1
    #         else:

            





print(isSubsequence("awedd","jnklj"))