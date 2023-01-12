def strStr(haystack: str, needle: str):
    if len(needle)>len(haystack):
        return -1
    if len(needle)==len(haystack): return 0
    i=0
    while i<len(haystack):
        # print(haystack[i])
        if haystack[i]==needle[0]:
            print(haystack[i:len(needle)+i])
            if haystack[i:len(needle)+i]==needle:
                return i

        i+=1
    return -1

# print(strStr(haystack = "sadbutsad", needle = "sad"))
# print(strStr(haystack = "leetcode", needle = "leeto"))
print(strStr(haystack = "mississippi", needle = "pi"))