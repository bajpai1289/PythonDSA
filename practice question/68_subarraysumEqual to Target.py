from collections import defaultdict

def subarray_sum(nums, k):
    sum_count = defaultdict(int)
    sum_count[0] = 1
    print(sum_count[3])
    sum = ans = 0
    for num in nums:
        sum += num
        ans += sum_count[sum - k]
        sum_count[sum] += 1
    return ans





print(subarray_sum(nums = [1,1,1], k = 2))
print(subarray_sum(nums = [1,2,3], k = 3))
print(subarray_sum(nums = [-5,5,4,-3,-2,-1,3,-2], k = 0))