def removeDuplicates(s: str):
    if not s:
        return ''
    stack = []
    for i in range(len(s)):
        if stack and s[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
   

    return "".join(stack)


         




print(removeDuplicates(s = "abbaca"))
print(removeDuplicates(s = "azxxzy"))