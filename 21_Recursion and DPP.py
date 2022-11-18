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
m='serendipitous'
n='precipitation'
# print(lcs_rec(m,n),len(m),len(n))

#using memoization
def lcs_memo(seq1,seq2):
    memo={}
    def recurse(idx1=0,idx2=0):
        key=(idx1,idx2)
        if key in memo:
            # print(memo)
            return memo[key]
        elif idx1==len(seq1) or idx2==len(seq2):
            memo[key]=0
        elif seq1[idx1]==seq2[idx2]:
            memo[key]=1+recurse(idx1+1,idx2+1)
        else:
            memo[key]=max(recurse(idx1+1,idx2),recurse(idx1,idx2+1))
        return memo[key]
    return recurse(0,0)    
# print(lcs_memo(m,n))

#CREATING A TABLE:
# n1=5
# n2=7
# table = [[0 for x in range(n2)] for y in range(n1)]
# print(table)

#using DP to solve this question
def lcs_dp(seq1, seq2):
    n1,n2=len(seq1),len(seq2)
    table=[[0 for i in range(n2+1)] for i in range(n1+1)]  #because we need an additional row to track the case where either of the sequence is empty
    for idx1 in range(n1):  #iterating over the rows
        for idx2 in range(n2): #iterating over the columns
            if seq1[idx1]==seq2[idx2]:
                table[idx1+1][idx2+1]=1+table[idx1][idx2]
            else:
                table[idx1+1][idx2+1]=max(table[idx1][idx2+1],table[idx1+1][idx2])
    return table[-1][-1] #return last row,column of the table


# print(lcs_dp(m,n))

def fact(n):
    memo={}
    def recurse(x=n):
        key=x
        if key in memo:
            print(memo)
            return memo[key]
        elif x==1:
            memo[key]=1
        else:
            memo[key]=x*recurse(x-1)
            print(memo)
        return memo[key]
    return recurse(n)


print(fact(7))
# n=1200
# arr=[1]
# for i in range(1,n+1):
#     arr.append(arr[i-1]*i)
# print(arr[-1])

# n=5000
# res=[0,1]
# for i in range(2,n):
#     res.append(res[i-1]+res[i-2])
# for i in res:
#     print(i)