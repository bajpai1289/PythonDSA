strs=["cba","daf","ghi"]
def minDeletionSize(strs):
    n=len(strs[0])
    res=[None]*n
    k=0
    for i in range(n):
        res[k]=list(map(lambda x:x[k], strs))
        k+=1
    print(res)
    count=0
    for l in res:
        flag = 0
        if(all(l[i] <= l[i + 1] for i in range(len(l)-1))):
            flag = 1

        # printing result
        if (flag) :
            continue
        else :
            count+=1
    return count

def goodWay(strs):
    count=0
    for i in zip(*strs):
        if list(i)==sorted(i):
            count+=1
    return count

print(minDeletionSize(strs))
    