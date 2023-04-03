def rotate(nums: list[int], k: int):
    l=len(nums)
    k=k%l
    n=l-k
    nums1 = nums[n:]+nums[:n]
    return nums1


print(rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(rotate([1,2],5))

tpl = [chr(i) for i in range(97,122)]
# new=tpl[2:]
print((tpl))