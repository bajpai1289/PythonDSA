#to find the distinction between the sliding window and two pointers, in two pointers we care about the two individial elements that the pointers are
#pointing at but in sliding window we care about the entire window
'Q. check if array is an pallindrome'
def checkPallindrome(nums: list[int]):
    l, r=0,len(nums)-1
    while l<=r:
        if nums[l]!=nums[r]:
            return False
        l+=1
        r-=1
    return True
    
'''Q. Given a sorted input array, return the two indices of the two elements whic
 sums up to the target value. there is exaclty one solution '''
def twoSum(nums: list[int], target:int):
    l,r=0, len(nums)-1
    while l<=r:
        if nums[l]+nums[r]>target:
            r-=1
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            return l,r
print(twoSum([-1,2,3,4,8,9],7))