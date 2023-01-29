def sortArrayByParity2(A: 'list[int]') -> 'list[int]':
    # s=0
    # e=len(nums)-1
    # while s<e:
    #     if nums[s]%2!=0:
    #         if nums[e]%2==0:
    #             nums[s],nums[e]=nums[e],nums[s]
    #             s+=1
    #             e-=1
    #         else:
    #             e-=1
    #     else:
    #         s+=1
    # return nums

    j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2:
            while A[j] % 2:
                j += 2
            A[i], A[j] = A[j], A[i]
    return A




print(sortArrayByParity2([4,2,5,7]))