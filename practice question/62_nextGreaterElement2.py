def nextLargerElement(arr):
    n=len(arr)
    #code here
    stack=[]
    stack.append(arr[-1])
    res=[0]*n
    res[-1]=-1
    for i in range(len(arr)-2,-1,-1):
        while stack and arr[i]>=stack[-1]:
            stack.pop()
        if len(stack)==0:
            res[i]=-1
        else:
            res[i]=stack[-1]
        stack.append(arr[i])
    return res
def nextGreaterElements(nums: list[int]) -> list[int]:
    nums=nums+nums
    return nextLargerElement(nums)[:len(nums)//2]




print(nextGreaterElements([1,2,1]))
print(nextGreaterElements([1,2,3,4,3]))
print(nextGreaterElements([1,5,3,6,8]))
