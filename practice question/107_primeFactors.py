def isPrime(n: int):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def findPrimeFactors(n: int):
    if isPrime(n):
        return 1, n
    primes = []
    for i in range(2,int(n**0.5)):
        if n%i==0 and isPrime(i):
            primes.append(i)
    return primes



#Efficient method to find the prime factorization
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

from math import gcd,lcm


def lcmManual(n: int, m: int):  
    self =12

    arr1= primeFactors(n)
    arr2= primeFactors(m)
    prod =1
    for i, j in zip(arr1, arr2):
        if i == j:
            prod*=(i)
        else:
            prod*=(i*j)
    return prod



print(lcm(5,10))
print(lcmManual(5,10))


print(lcm(8,12,24))
# print(findPrimeFactors(13))
# print(findPrimeFactors(64))
# print(findPrimeFactors(12))
# print(findPrimeFactors(1885583700))
# print(primeFactors(64))
# print(primeFactors(12))
# print(primeFactors(1885583700))

# st = "array"
# st2= st
# print(st)


def HCF(a, b):
    while a%b>0:
        r=a%b
        a=b
        b=r
    return b

print(gcd(8,10)==HCF(8,10))