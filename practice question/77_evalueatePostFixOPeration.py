def evalRPN(tokens: list[str]) -> int:
    result=[]
    for i in range(len(tokens)):
        # print(result)
        try:
            result.append(int(tokens[i]))
        except:
            if tokens[i]=='+':
                num=result.pop()
                result[-1]+=num
            if tokens[i]=='':
                num=result.pop()
                result[-1]-=num
            if tokens[i]=='*':
                num=result.pop()
                result[-1]*=num
            if tokens[i]=='/':
                num=result.pop()
                result[-1]=int(result[-1]/num)
    return result


print(evalRPN(["4","3","-"]))
# print(evalRPN(["2","1","+","3","*"]))
# print(evalRPN(["4","13","5","/","+"]))
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))