str1='rgewrgFFF=-egewergRR'
real=''
for i in range(len(str1)):
    if ord(str1[i])>=97 and ord(str1[i])<=122:
        real+=(chr(ord(str1[i])-32))
    else:
        real+=(str1[i])
print(real)

