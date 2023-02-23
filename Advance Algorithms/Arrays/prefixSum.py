'design a data structure that can query the sum of a subarray of the values'
class prefixSum:
    def __init__(self, nums:list[int]) -> None:
        self.prefix=[]
        total =0
        for n in nums:
            total+=n
            self.prefix.append(total)
    
    def rangeSum(self, left, right):
        preRight=self.prefix[right]
        preLeft=self.prefix[left] if left>0 else 0
        return preRight-preLeft
     
