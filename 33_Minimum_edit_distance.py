# str1='intention'
# str2='execution'
str1='intention'
str2='exception'

output1=5
# function signature
def min_steps0(str1, str2):
    pass


'''
test cases:
1. general case
2. no change is required
3. all the characters need to be changed
4. check both strings of equal length 
5. unqual length
6. on of the string is empty
7 only require, deletion, addition or swap
'''

# Step 1: Brute force solution(recursive)
'''
-- if the first character is equal ignore the both
-- if the first character is not equal:
    -either it has to be deleted:
       • 1 + recursively solve after ignoring first character of str1
    -or swapped 
        • 1 + recursively solve after ignoring the first character of each
    -or a character inserted before it
        •  1 + recursively solve after ignoring the first character of str2
'''

def min_steps(str1, str2,i1=0,i2=0):
    if i1==len(str1):
        return len(str2)-i2
    elif i2==len(str2):
        return len(str1)-i1
    elif str1[i1]==str2[i2]:
        return min_steps(str1,str2,i1+1,i2+1)
    else:
        return 1 + min(min_steps(str1,str2,i1+1,i2),  #deleting
                       min_steps(str1,str2,i1+1,i2+1), #swapping
                       min_steps(str1,str2,i1,i2+1))   #insertion

        
# print(min_steps(str1,str2))



#Memoized solution
'''before starting with the computation we check if the solution of that comutation os already present in the memo
'''
def min_steps_memo(str1, str2):
    memo={}
    def recurse(i1=0,i2=0):
        key=i1,i2
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key]=len(str2)-i2
        elif i2==len(str2):
            memo[key]=len(str1)-i1
        elif str1[i1]==str2[i2]:
            memo[key]=recurse(i1+1,i2+1)
        else:
            memo[key]=1+min(recurse(i1+1),
                            recurse(i1+1,i2+1),
                            recurse(i1,i2+1))
        return memo[key]
    return recurse()

# print(min_steps_memo(str1, str2))

'''Dynamic Programming solution'''
table=[[0 for _ in range(len(str1)+1)] for x in range(len(str2)+1)]

print(table)