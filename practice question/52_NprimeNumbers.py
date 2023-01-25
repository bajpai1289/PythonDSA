def isPrime(n: int):
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True
arr=[i for i in range(2,1000) if isPrime(i)]
# for i in range(2, 9):
#     for j in arr:
#         if j%i==0:
#             arr.remove(j)

print(arr[:8])