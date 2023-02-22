def firstMissingPositive(nums: list[int]):
    target = 1
    i=0
    while(i<len(nums)):
        print("nums is  : ", nums)
        print("nums at i is  : ", nums[i])
        print("target is: ",target)
        if target==nums[i]:
            # print(target,nums[i], i)
            i=0
            target+=1
            print("target increased")
        else: 
            i+=1
    return target


# print(firstMissingPositive([1,2,0]))
# print(firstMissingPositive([3,4,-1,1]))
# print(firstMissingPositive([7,8,9,11,12]))
# print(firstMissingPositive([4,2,-1,1]))
print(firstMissingPositive(nums= [2,1]))