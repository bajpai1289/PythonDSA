def recursivFactorial(n: int):
    if n==1:
        return 1
    return n*recursivFactorial(n-1)

# print(recursivFactorial(5555))

def dynamicFactorial(n: int):
    arr=[1]
    for i in range(2,n+1):
        arr.append(arr[-1]*i)
    return arr[-1]
print(dynamicFactorial(6))

def permutation_recursively(nums: list[int]):
    return helper(0, nums)

def helper(i: int, nums: list[int])->list[list[int]]:
    if i == len(nums):
        return [[]]

    resPerms=[]
    perms = helper(i+1, nums)
    for p in perms:
        for j in range(len(p)+1):
            pCopy=p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms

print(permutation_recursively([1,2,3,4]))
