# class tictactoe:
#     def __init__(self,n =3) -> None:
#         self.board = [[None for i in range(n)] for i in range(n)]
#         self.noneCount = 9

#     def move(self, x: int, y:int, player: int):
#         def win(board):
#             #rows
#             c1=(board[0][0]==board[0][1]==board[0][2]) and ( board[0][0] is not None or  board[0][1] is not None or  board[0][2] is not None)
#             c2=(board[1][0]==board[1][1]==board[1][2]) and ( board[1][0] is not None or  board[1][1] is not None or  board[1][2] is not None)
#             c3=(board[2][0]==board[2][1]==board[2][2]) and ( board[2][0] is not None or  board[2][1] is not None or  board[2][2] is not None)
#             #column
#             c4=(board[0][0]==board[1][0]==board[2][0]) and ( board[0][0] is not None or  board[1][0] is not None or  board[2][0] is not None)
#             c5=(board[0][1]==board[1][1]==board[2][1]) and ( board[0][1] is not None or  board[1][1] is not None or  board[2][1] is not None)
#             c6=(board[0][2]==board[1][2]==board[2][2]) and ( board[0][2] is not None or  board[1][2] is not None or  board[2][2] is not None)
#             #diagona
#             c7=(board[0][0]==board[1][1]==board[2][2]) and ( board[0][0] is not None or  board[1][1] is not None or  board[2][2] is not None)
#             c8=(board[0][2]==board[2][1]==board[2][0]) and ( board[0][2] is not None or  board[2][1] is not None or  board[2][0] is not None)
#             if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
#                 return True
#             else:
#                 return False
#         self.board[x][y]=player
#         self.noneCount-=1
#         if win(self.board):
#             print(player,'has won')
#             return player
#         if self.noneCount==0:
#             print('no player won')
#             return None

    

# toe=tictactoe(3)
# toe.move(0, 0, 1)
# # ; -> Returns 0 (no one wins)
# # |X| | |
# # | | | |    // Player 1 makes a move at (0, 0).
# # | | | |

# toe.move(0, 1, 1)
# # ; -> Returns 0 (no one wins)
# # |X| |O|
# # | | | |    // Player 2 makes a move at (0, 2).
# # | | | |

# toe.move(0, 2, 2)
# # ; -> Returns 0 (no one wins)
# # |X| |O|
# # | | | |    // Player 1 makes a move at (2, 2).
# # | | |X|

# toe.move(1, 0, 2)
# # ; -> Returns 0 (no one wins)
# # |X| |O|
# # | |O| |    // Player 2 makes a move at (1, 1).
# # | | |X|

# toe.move(1, 1, 1)
# # ; -> Returns 0 (no one wins)
# # |X| |O|
# # | |O| |    // Player 1 makes a move at (2, 0).
# # |X| |X|

# toe.move(1, 2, 1)#; -> Returns 0 (no one wins)
# # |X| |O|
# # |O|O| |    // Player 2 makes a move at (1, 0).
# # |X| |X|

# toe.move(2, 0, 1)
# toe.move(2, 1, 2)
# toe.move(2, 2, 2)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# print(toe.board)


#refactored program
class TicTacToe:
    def __init__(self, n=3):
        self.board = [[None for i in range(n)] for j in range(n)]
        self.noneCount = n ** 2

    def move(self, x, y, player):
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            raise ValueError("Invalid move: x and y values must be between 0 and {}.".format(len(self.board)-1))
        if player not in [1, 2]:
            raise ValueError("Invalid player: player value must be 1 or 2.")

        if self.board[x][y] is not None:
            print("Invalid move: the cell ({}, {}) is already occupied.".format(x, y))
            return

        self.board[x][y] = player
        self.noneCount -= 1

        if self.check_win(player):
            print("Player {} has won!".format(player))
            return player
        elif self.noneCount == 0:
            print("The game ended in a tie!")
            return None

    def check_win(self, player):
        for i in range(len(self.board)):
            # check rows
            if all(cell == player for cell in self.board[i]):
                return True
            # check columns
            if all(row[i] == player for row in self.board):
                return True
        # check diagonals
        if all(self.board[i][i] == player for i in range(len(self.board))):
            return True
        if all(self.board[i][len(self.board)-i-1] == player for i in range(len(self.board))):
            return True
        return False

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) if cell is not None else "-" for cell in row))
game = TicTacToe()
game.move(0, 0, 1)
game.move(0, 1, 2)
game.move(1, 1, 1)
game.move(0, 2, 2)
game.move(2, 2, 1)
game.print_board()



