def interpret(command: str):
    # newString=command.replace("()", "o")
    # newString=newString.replace("(al)", "al")
    # return newString
    result =''
    for i in range(len(command)-1):
        if command[i]=='G' or command[i]=='g':
            result+='G'
            i+=1
        
        elif command[i]=='(' and command[i+1]==')':
            result+='o'
            i+=1
        elif command[i]=='(' and command[i+1]=='a':
            result+='al'
            i+=2
        # print(command[i], command[i+1])
    return result





print(interpret("G()()()(al)(al)(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))