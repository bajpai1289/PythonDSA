def minimumDiff(nums: list[int])->list[int]:
    nums.sort()
    minDiff=float('inf')
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]<minDiff:
            minDiff=nums[i+1]-nums[i]
    return minDiff

def inOrder(root):
    if root is None:
        return []
    return inOrder(root.left)+[root.val]+inOrder(root.right)


print(minimumDiff([1,21,52,65,41,5,555,47,6332]))