poly1=[3,2]  #TODO: len(poly1)<=len(poly2)
poly2=[2,4]
# output=[6, 8, 19, 41, 38, 14]
# def multiplyPoly(poly1, poly2):
n1,n2=len(poly1),len(poly2)
res=[0]*(n1+n2-1)
x=[[None for _ in range(n2)] for t in range(n2) ]
for i in range(n1):
    for j in range(n2):
        # print(i,j)
        x[i][j]=poly1[i]*poly2[j]

for k in range(len(res)):
    for i in range(n1):
        for j in range(n2):
            if i+j==k:
                res[k]+=x[i][j]


print(res)















# print(multiplyPoly(poly1,poly2))