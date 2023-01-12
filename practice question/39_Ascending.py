s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
s=[i for i in s.split()]
res=[]
for i in s:
    try:
        res.append(int(i))
    except:
        pass
print(res)