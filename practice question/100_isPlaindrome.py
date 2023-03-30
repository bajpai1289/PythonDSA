# def isPalindrome(strs: str):
#     return [i.lower() for i in strs if i.isalnum()]==[i.lower() for i in strs if i.isalnum()][::-1]
def isPalindrome(strs): return [i.lower() for i in strs if i.isalnum()]==[i.lower() for i in strs if i.isalnum()][::-1]

print(isPalindrome('A man, a plan, a canal. Panama'))
print(isPalindrome('My age is 0, 0 si ega ym.'))
print(isPalindrome('1 eye for of 1 eye.'))
print(isPalindrome('0_0 (: /-\ :) 0-0'))
print(isPalindrome('eye'))
print(isPalindrome('_eye'))