'''TLE soluttion''' 
# def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
#     def countVowel(lt: list[str]):
#         vowels={
#             'a',
#             'e',
#             'i',
#             'o',
#             'u'
#         }
#         count=0
#         for i in lt:
#             if i[0] in vowels and i[-1] in vowels:
#                 count+=1
#         return count
#     result = []
#     for start, end in queries:
#         result.append(countVowel(words[start:end+1]))
#     return result

def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    prefixSum=[0]
    vowels={'a', 'e', 'i', 'o', 'u'}

    for i in words:
        if i[0] in vowels and i[-1] in vowels:
            if not prefixSum:
                prefixSum.append(1)
            else:
                prefixSum.append(prefixSum[-1]+1)
        else:
            if not prefixSum:
                prefixSum.append(1)
            else:
                prefixSum.append(prefixSum[-1])
    result =[]
    print('prefix sum: ',prefixSum)
    for start, end in queries:
        result.append(prefixSum[end+1]-prefixSum[start])
    return result
    

print(vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
# print(vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))