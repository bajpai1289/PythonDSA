def findJudge(n: 'int', trust: 'list[list[int]]'):
    trustMap={}  #key trusts value
    for i in trust:
        trustMap[i[0]]=i[1]
    print(trustMap)
    sett={i for i in trustMap.values()}
    judge=[]
    for i in sett:
        if i not in trustMap.keys():
            judge.append(i)
    print(sett)
    return judge






 


# print(findJudge(2,[[1,2]]))
# print(findJudge(3,[[1,3],[2,3]]))
print(findJudge(3,[[1,2],[2,3]]))
print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
# print(findJudge(3,[[1,3],[2,3],[3,1]]))