def validParenthesis(s):
    stack=[]
    opening=['{','[','(']
    # closing2=[('{','}'), ('[',']'),('(',')')]
    closing=['}', ']',')']
    for i in range(len(s)):
        if s[i] in opening:
            stack.append(s[i])
        else:
            while stack:
                if stack[-1]==:
                    break
                stack.pop()
            return False
    if len(stack)>0:
        return False
    else: return True 

print(validParenthesis('([)]'))