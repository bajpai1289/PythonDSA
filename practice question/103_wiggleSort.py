from collections import deque
class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums=nums
    
    def wiggleSort(self) -> None:
        tmp2 = deque(sorted(self.nums, reverse=True))
        tmp1 = deque(sorted(self.nums))
        self.nums.clear()
        for i in range(0,len(tmp2)-1,2):
            self.nums.append(tmp1[i])
            self.nums.append(tmp2[i+1])


obj = Solution([1,5,1,1,6,4,3])
obj.wiggleSort()
print(obj.nums)

# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6]