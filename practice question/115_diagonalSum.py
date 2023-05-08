def diagonalSum(mat: list[list[int]]):
    n = len(mat)
    #calculating for diagonal 1: its correct
    diag1 = 0
    for i in range(n):
        diag1+=mat[i][i]
    # print("diagonal 1: ", diag1)
    # caclucating diagonal 2
    diag2 =0
    for r in range(n):
        c=len(mat)-1-r
        # print(r, c)
        diag2+=mat[r][c]
    # print("diagonal 2: ", diag2)
    
    _sum = diag1+diag2
    if len(mat)%2!=0:
        center = len(mat)//2
        _sum-=mat[center][center]
    return _sum

# more optimized
def diagonalSum(mat: list[list[int]]):
        n = len(mat)
        _sum=0
        for i in range(n):
            # primary diagonal
            _sum+=mat[i][i]
            # secondary diagonal
            _sum+=mat[i][n-i-1]
        if n%2!=0:
            _sum-=mat[n//2][n//2]
        return _sum



print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))