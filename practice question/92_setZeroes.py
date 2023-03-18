matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
def setZeroes(matrix: 'list[list[int]]') -> None:
    indexes=set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):          
            if matrix[r][c]==0:
                indexes.add((r,c))
    rows=[]
    cols=[]
    for row, col in indexes:
        rows.append(row)
        cols.append(col)
    r,c=0,0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):  
            if (r, c) in indexes:
                matrix[r][c]=0
            if c in cols:
                matrix[r][c]=0




setZeroes(matrix)
print(matrix==[[0,0,0,0],[0,4,5,0],[0,3,1,0]])