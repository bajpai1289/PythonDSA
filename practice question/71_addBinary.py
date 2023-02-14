def addBinary(a: str, b: str) -> str:
    def parseBinary(n: int):
        res=''
        while n>1:
            res+=str(n%2)
            n//=2
        return (res+str(n))[::-1]
    def parseInteger(n: str):
        q=0
        n=n[::-1]
        for i in range(len(n)):
            q+=int(n[i])*(2**i)
        return q
    return parseBinary(parseInteger(a)+parseInteger(b))


print(addBinary(a = "11", b = "1"))
