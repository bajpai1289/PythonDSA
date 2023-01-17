# from functools import cache
# @cache
def minFlipsMonoIncr(s: str, idx=0) -> int:
    # testCondition=all(s[i]<=s[i+1] for i in range(len(s)-1))
    # if testCondition:
    #     return 0
    if idx==len(s):
        return 0
    else:
        #we do nat flip the bit
        option1= minFlipsMonoIncr(s,idx+1)
        #we do flip the bit
        option2=1+minFlipsMonoIncr(s,idx+1)
        # print(option1, option2)
        return 1+min(option1, option2)
    
    
    




print(minFlipsMonoIncr("00110"))
print(minFlipsMonoIncr(s = "010110"))
print(minFlipsMonoIncr(s = "00011000"))