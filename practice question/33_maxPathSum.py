def maxSumPath(arr1: list[int], arr2:list[int],m,n):
    sum1, sum2=0,0
    commonElement=None
    for i in arr1:
        if i in arr2:
            commonElement=i
            break
    indexat1=arr1.index(commonElement)
    indexat2=arr2.index(commonElement)
    sum_arr1=sum(arr1)
    sum_arr2=sum(arr2)
    #passing through array 1 and switching to array 2 to at common element:

    # for i in range(m):
    #     # print(arr1[i], end=", ")
    #     sum1+=arr1[i]
    #     if i == indexat1:
    #         break
    # sum1+=sum(arr2[indexat2+1:])
    sum1+=sum(arr1[:indexat1])
    sum1+=sum(arr2[indexat2:])
    # print(arr2[indexat2+1:])

    

    #passing through array 2 and switching to array 1 at common element
    sum2+=sum(arr2[:indexat2])
    sum2+=sum(arr1[indexat1:])
    # for i in range(n):
    #     # print(arr2[i], end=", ")
    #     sum2+=arr2[i]
    #     if i == indexat2:
    #         break
    # sum2+=sum(arr1[indexat1+1:])
    # print(arr2[indexat1+1:])
    return max(sum1, sum2, sum_arr1, sum_arr2)






# print(maxSumPath([2,3,7,10,12],[1,5,7,8],5,4))
# print(maxSumPath([2,3,5,7,10,12],[1,5,7,8],6,4))
print(maxSumPath([2,4,5,8,10],[4,6,8,9],5,4))
# print(maxSumPath([1,2,3],[3,4,5],3,3))

