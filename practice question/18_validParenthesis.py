def validParenthesis(s):
    stack=[]
    lookup={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for i in s:
        print(stack)
        if i in lookup.values():
            stack.append(i)
        elif stack and stack[-1]==lookup[i]:
            stack.pop()
        else:
            return False
    return stack==[]

print(validParenthesis('{[()()[]]}'))