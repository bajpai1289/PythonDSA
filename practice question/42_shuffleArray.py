def shuffle(nums: list[int], n: int):
    result = [0] * (2 * n)
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[n + i]
    return result

    
    arr1=nums[:n]
    arr2=nums[n:]
    # print(arr1,arr2)
    # for i in range(2*n):

    res=[None]*(n*2)
    k=0
    for i in range(len(res)):
        print(res)
        if i%2==0:
            res[i]=arr1[k]
            k+=1
        else:
            res[i]=arr2[k]
            k+=1
    return res    

s="thisis"
print(s.index('i'))
print(shuffle(nums = [2,5,1,3,4,7], n = 3))
print(shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(shuffle(nums = [1,1,2,2], n = 2))
