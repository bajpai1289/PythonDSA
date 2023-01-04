
def climbStairs(n: int)->int:
    dp=[None]*(n+1)
    dp[0]=1
    dp[1]=2
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-2]




print(climbStairs(4))

# def fib(n: int):
#     res=[None]*(n+1)
#     res[0]=0
#     res[1]=1
#     for i in range(2,n+1):
#         res[i]=res[i-1]+res[i-2]
#     print(res)


# print(fib(0))