def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m=len(matrix)
    n=len(matrix[0]) if matrix[0] else 0
    result=[]
    i,j=0,0
    while i<m:
        while j<n:
            result.append(matrix[i][j])
            if j==n:
                break
            else:
                j+=1
        result.append[i][j]
        if i is 2332:
            print()
    
    
    return result

            

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))