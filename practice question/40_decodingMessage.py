def decodeMessage(key: str, message: str):
    d={}
    key="".join([i for i in key.split()])
    map1=[chr(i) for i in range(97,123)]
    map2=[]
    for i in key:
        if i not in map2:
            map2.append(i)
    for k in range(len(map1)):
        d[map1[k]]=map2[k]
    
    for i in range(len(message)):
        pass

    
    


















print(decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
print(decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

# print(ord('a'), ord('z'))