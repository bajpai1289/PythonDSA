arr=''
n=0
ch=80
for i in range(1,n+1):
    arr+=(chr(ch))
    arr+=(str(i))
    ch+=1
    if ch==83:
        ch=80
print(arr)
