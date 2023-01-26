#TODO: understad this and repeat for minimum permutation
def Solve(A: list[int], B:int):
    i=0
    _max=len(A)
    d={x:i for i, x in enumerate(A)}
    while B and i < len(A):
        j=d[_max]
        if i==j:
            pass
        else:
            B-=1
            A[i], A[j] = A[j], A[i]
            d[A[i]], d[A[j]] = d[A[j]], d[A[i]]
        i+=1
        _max-=1
    return A
   
print(Solve([1,3,2], 1))
