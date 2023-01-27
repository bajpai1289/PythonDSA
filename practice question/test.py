arr=[str(i) for i in range(100,1000) if i%5==0]
for i in arr:
    if all(int(c)%2==0 for c in i)