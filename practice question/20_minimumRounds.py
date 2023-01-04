def minimumRounds(tasks: list[int]):
    d={}
    for i in tasks:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    print(d)

print(minimumRounds([2,2,3,3,2,4,4,4,4,4]))