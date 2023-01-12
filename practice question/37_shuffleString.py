def restoreString(s: str, indices: list[int]) -> str:
    resultArr=[None]*len(indices)
    for i in range(len(indices)):
        resultArr[indices[i]]=s[i]
    return "".join(resultArr)








print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(restoreString(s = "abc", indices = [0,1,2]))