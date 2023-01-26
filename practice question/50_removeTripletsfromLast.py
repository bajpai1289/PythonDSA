def removeTriplets(arr: 'list[int]'):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for k, v in d.items():
        if v>3:
            pass
    return arr
            
    
    










# print(removeTriplets([2,2,3,2,3,2]))
# print(removeTriplets([2,4,2,2,7,5,6,7,8,6,6,2,6,7,6]))
# def fun(num):
#     if num==1:
#         return 8
#     else:
#         return (6*(num**2))+(2*num)+fun(num-1)
    
# print(fun(99))
def max_power_of_array_pair(A: 'list[int]', B: 'list[int]'):
    A.sort()
    B.sort()
    count = 0
    for i in range(len(A)):
        if A[i]==B[i]:
            count+=1
    return count

A = [2,1,1]
B = [1,2,2]
print(max_power_of_array_pair(A, B))
