def longestConsecutive(nums: list[int]) -> int:
    numsSet=set(nums)
    longest=0
    for n in nums:
        #if its start of the sequence 
        if (n-1) not in numsSet:
            length=0
            while n+length in numsSet:
                length+=1
            longest=max(length,longest)
    return longest




print(longestConsecutive([100,4,200,1,3,2]))
import sys
a=sys.maxsize
print(a)