def calPoints(operations: list[str]) -> int:
    for i in range(len(operations)):
        try:
            operations[i]=int(operations[i])
        except: pass
    stack=[]
    for i in operations:
        if isinstance(i, int):
            stack.append(i)
        elif i=='C':
            stack.pop()
        elif i=='D':
            stack.append(stack[-1]*2)
        elif i=='+':
            stack.append(stack[-1]+stack[-2])
    return sum(stack)

print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))
print(calPoints(["1","C"]))

# print(isinstance("-2", int))

