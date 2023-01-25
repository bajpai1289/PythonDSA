def getConcatenation(nums: list[int]):
    ans= [None]*(2*len(nums))
    n=len(nums)
    for i in range(len(ans)):
        ans[i] = nums[i%n]
    return ans

print(getConcatenation([1,3,2,1]))