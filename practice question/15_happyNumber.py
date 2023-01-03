class Solution:
    def isHappy(n: int):
        endingCondition = [0,2,3,4,5,6,7,8,9]
        result=sum(list(map(lambda x:x**2, [int(i) for i in str(n)])))
        if result==1:
            return True
        elif result in endingCondition:
            return False
        else:
            return Solution.isHappy(result)

print(Solution.isHappy(16))