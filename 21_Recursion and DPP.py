#Longest common subsequence main problem
##using recursion
def lcs_rec(seq1,seq2,idx1=0,idx2=0):
    if idx1==len(seq1) or idx2==len(seq2):
        return 0
    elif seq1[idx1]==seq2[idx2]:
        return 1+lcs_rec(seq1,seq2,idx1+1,idx2+1)
    else:
        option1=lcs_rec(seq1,seq2,idx1+1,idx2)
        option2=lcs_rec(seq1,seq2,idx1,idx2+1)
        return max(option1,option2)
    
# m="AGGTAB"
# n="GXTXAYB"
m='qwqawexqqwqwwswrq'
n='knuokojokimpopppo'
# print(lcs_rec(m,n),len(m),len(n))

#using memoization
def lcs_memo(seq1,seq2):
    memo={}
    def recurse(idx1=0,idx2=0):
        key=(idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key]=0
        elif seq1[idx1]==seq2[idx2]:
            memo[key]=1+recurse(idx1+1,idx2+1)
        else:
            memo[key]=max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)    
print(lcs_memo(m,n))