def countBits(n: int):
    arr=list(range(n+1))
    for i in range(n+1):
        arr[i]=arr[i].bit_count()
    return arr

print(countBits(2))
print(countBits(5))