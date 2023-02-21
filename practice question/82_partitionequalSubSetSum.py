def canPartition(nums: list[int]) -> bool:
    _sum=sum(nums)
    memo={}
    def recurse(arr:list[int], target: int, length: int):
        if length==0:
            return True
        if (target, length) in memo:
            return memo[(target, length)]
        else:
            if arr[length-1]==target:
                memo[(target,length)] = recurse(arr,target,length-1) or recurse(arr,target-arr[length-1],length-1)
                return memo[(target, length)]
            else:
                return recurse(arr, target, length-1)
        
    if _sum%2!=0: return False
    else:
        return recurse(nums, _sum//2, len(nums))


        


print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
from collections import Counter
str1='aaabccc'
d=dict(Counter(str1))
print(d)