def findJudge(n: int, trust: list[list[int]]):
    if not trust:
        if n==1:
            return 1
        else:
            return -1
    d={}
    for i in trust:
        if i[1] in d:
            d[i[1]].append(i[0])
        else:
            d[i[1]]=[i[0]]
    notJudges=set()
    for i in d.values():
        notJudges.update(i)
    # print(notJudges)
    potential=set(range(1, n+1))-notJudges
    if not potential:
        return -1
    while potential:
        judge=potential.pop()
        if judge in d:
            if len(d[judge])==n-1:
                return judge
    return -1
        

print(findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])==-1)
print(findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])==3)
print(findJudge(n = 3, trust = [[1,3],[2,3]])==3)
print(findJudge(n = 3, trust = [[1,2],[2,3]])==-1)
