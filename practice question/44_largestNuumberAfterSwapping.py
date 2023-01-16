def largestInteger(num: int):
    num=str(num)
    enum, onum=[],[]
    for i in range(len(num)):
        if i%2==0:
            enum.append(num[i])
        else:
            onum.append(num[i])
    enum.sort(reverse=True)
    onum.sort(reverse=True)
    print(enum, onum)
    result=[None]*len(enum+onum)
    result[1::2] = onum
        # print(largesprint(largestInteger(65875)==87655)
    result[::2] = enum
    return int(''.join(result))
print(largestInteger(247))
'''
is tjiz the real life is this just fanatasy
'''