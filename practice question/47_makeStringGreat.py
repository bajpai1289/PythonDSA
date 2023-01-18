def makeGood(s: str):
    if not s:
        return True
    stack:list[str]=[]
    for i in range(len(s)):
        print(stack)
        if stack and ((stack[-1].isupper() and s[i].islower()) or (stack[-1].islower() and s[i].isupper())):
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)
            
        



# print(makeGood("mC"))
print(makeGood("abBAcC"))
# print(makeGood("s"))