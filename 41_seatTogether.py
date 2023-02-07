def seats(A: str):
    crosses = [i for i, c in enumerate(A) if c=='x']
    crosses=[(cross-i) for i, cross in enumerate(crosses)]
    print(crosses)

    n=len(crosses)
    if n==0:
        return 0
    ans = float('inf')
    
    for segment_start in range(len(A)):
        total =0
        for cross in crosses:
            total+=abs(cross-segment_start)
            
        ans = min(ans, total)
    return ans 
def seatsOPtimized(A: str):
    crosses = [i for i, c in enumerate(A) if c=='x']
    crosses=[(cross-i) for i, cross in enumerate(crosses)]
    print(crosses)

    n=len(crosses)
    if n==0:
        return 0
    ans = float('inf')

    segment_start= crosses[n//2]
    for cross in crosses:
        total+=abs(cross-segment_start)
        
    ans = min(ans, total)
    return ans 

# for i in range(-9,1):
#     print(i, end=' ')


print(seats('.x..x..xx.'))