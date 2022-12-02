# a='1010'
# b='1011'
# a='11'
# b='1'
# a=a[::-1]
# b=b[::-1]
# int1,int2=0,0
# for i in range(len(a)):
#     int1=int1+(int(a[i]))*(2**i)
# for i in range(len(b)):
#     int2=int2+(int(b[i]))*(2**i)
# result=str(bin(int1+int2))

# print(result[2:])
# # bin()
# result=int(result[2:])

# res=[]
# while result>0:
#     result//=2
#     res.append(result%2)

# print(''.join(map(str,res)))
a=3
b=3
a*=-1

diff=a-b
print(diff*(-1))
