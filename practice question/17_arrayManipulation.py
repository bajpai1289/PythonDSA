# def heightChecker(heights: list[int]):
#     expected=heights.copy()
#     expected.sort()
#     count=0
#     for i in range(len(expected)):
#         if expected[i]!=heights[i]:
#             count+=1
#     return count

# print(heightChecker([5,1,2,3,4]))
def fun1(n):
    x=0
    while n>0:
        x+=fun1(n)
        n-=1
    return n

def fun2(n):
    x=0
    while n>0:
        x+=fun1(n-1)
    return n

# fun1(3)
fun2(3)
 