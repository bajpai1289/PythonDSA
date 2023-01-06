# def findDisappearedNumbers(nums: list[int]):
#     nums=set(nums)
#     res=[]
#     target=[i for i in range(1,len(nums)+1)]
#     # print(target,nums)
#     for i in target:
#         if i not in nums:
#             res.append(i)

#     return res
#     # return target

# print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
# print(findDisappearedNumbers([1,1]))

def match(s: str, p: str) -> bool:
    # base case: if the pattern is empty, the string must also be empty for a match to occur
    if not p:
        return not s

    # check for a match of the first character of the string with the first character of the pattern
    first_match = bool(s) and p[0] in {s[0], '.'}

    # if the pattern has more than one character and the second character is '*'
    if len(p) >= 2 and p[1] == '*':
        # check for a match by either:
        # - matching the '*' to zero characters and moving on to the next pattern character
        # - matching the '*' to one or more characters and trying to match the rest of the pattern to the rest of the string
        # - matching the '*' to zero or more characters and trying to match the pattern to the rest of the string
        return match(s, p[2:]) or (first_match and match(s[1:], p)) or match(s, p[1:])
    else:
        # if the pattern has no '*' or it has a '*' but the first characters don't match,
        # move on to the next character in both the string and the pattern and check for a match
        return first_match and match(s[1:], p[1:])

print(match('ab', '.*'))

