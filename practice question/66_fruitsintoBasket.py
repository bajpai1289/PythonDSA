def totalFruit(fruits: list[int]):
    d={}
    for i in fruits:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d=dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    count = 0
    total=0
    print(d)
    for i, j in d.items():
        total+=j
        count+=1
        if count==2:
            break
    return total

        

# print(totalFruit([1,2,1]))
# print(totalFruit([0,1,2,2]))
# print(totalFruit([1,2,3,2,2]))
print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
