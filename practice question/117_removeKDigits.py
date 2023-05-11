def removeKdigits(num: str, k: int) -> str:
    # using a monotonic stack
    stack = []
    for n in num:
        while stack and k>0 and stack[-1] > n:
            stack.pop()
            k -= 1
        if stack or n != '0': 
            stack.append(n)       
    if k:
        stack=stack[0:-k]     
    return ''.join(stack) or '0'  

print(removeKdigits(num = "1432219", k = 3))
print(removeKdigits(num = "10200", k = 1))
# print(removeKdigits())