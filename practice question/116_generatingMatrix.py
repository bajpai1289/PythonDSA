def generateMatrix(n: int):
    res=[]
    i=1
    while i<n*n+1:
        temp=[]
        for j in range(n):
            temp.append(i)
            i+=1
        res.append(temp)
    return res


print(generateMatrix(1))
print(generateMatrix(2))
print(generateMatrix(3))
print(generateMatrix(4))
print(generateMatrix(5))