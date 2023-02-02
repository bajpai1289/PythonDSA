def seats(A: str):
    MOD=10000003
    crosses = [i for i, c in enumerate(A) if c=='x']
    crosses=[(cross-i) for i, cross in enumerate(crosses)]

    n=len(crosses)
    if n==0:
        return 0
    ans = float('inf')
    for segment_start in range(len(A)):
        total =0
        for cross in crosses:
            total+=abs(cross-segment_start)
            total%=MOD
        ans = min(ans, total%MOD)
    return ans 

# for i in range(-9,1):
#     print(i, end=' ')


print(seats('..x.x..x.x...x.x.x.x...x..x.x.xx.x.'))