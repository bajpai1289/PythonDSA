def lcmAndGcd(n: int , m: int):
    def primeFactors(n: int):
        c =2
        res=[]
        while n>1:
            if n%c ==0:
                res.append(c)
                n/=c
            else:
                c+=1
        return res
    # code here 
    res=[]
    arr1= primeFactors(n)
    arr2= primeFactors(m)
    LCM =1
    HCF =1
    for i, j in zip(arr1, arr2):
        if i == j:
            LCM*=(i)
        else:
            LCM*=(i*j)
    res.append(LCM)
    print(arr1, arr2)
    for k, m in zip(arr1, arr2):
        print(k,m)
        if k==m:
            HCF*=k
    res.append(HCF)

    return res


print(lcmAndGcd(5,10))

