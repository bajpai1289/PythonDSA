def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    d={}
    ptr1 = 0
    ptr2 =0
    globCount = 0
    while ptr2<len(s):
        ptr2 = ptr1+k
        currCount =0
        for i in s[ptr1: ptr2]:
            # print(s[ptr1: ptr2])
            if i in vowels:
                currCount+=1
            # print(currCount)
        globCount = max(currCount, globCount)
        ptr1+=1
    return globCount
        
        




# print(maxVowels(s = "abciiidef", k = 3))
# print(maxVowels(s = "aeiou", k = 2))
