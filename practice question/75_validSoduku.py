#we'll use a hashset
from collections import defaultdict
def isValidSudoku(board: list[list[str]]) -> bool:
    cols=defaultdict(set)
    rows=defaultdict(set) #its a hashset key= column numbner value: set representing all particular numbers in this column
    squares=defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c]=='.':
                continue

            if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r//3, c//3)]):  #the current row that we are in(rows is hour hasmap the key is the current node that we are in, )
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True



print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))



print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))