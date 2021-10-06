EMPTY = "-"
ROOK = "R"
PAWN = "P"
BISHOP = "B"
KNIGHT = "N"
KING = "K"
QUEEN = "Q"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][3] = KING
board[7][3] = KING
board[0][4] = QUEEN
board[7][4] = QUEEN
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT
board[0][2] = BISHOP
board[0][5] = BISHOP
board[7][2] = BISHOP
board[7][5] = BISHOP
board[1][0] = PAWN
board[1][1] = PAWN
board[1][2] = PAWN
board[1][3] = PAWN
board[1][4] = PAWN
board[1][5] = PAWN
board[1][6] = PAWN
board[1][7] = PAWN
board[6][0] = PAWN
board[6][1] = PAWN
board[6][2] = PAWN
board[6][3] = PAWN
board[6][4] = PAWN
board[6][5] = PAWN
board[6][6] = PAWN
board[6][7] = PAWN

for i in range(len(board)):
    print(board[i])
    print()




LIST COMPREHENSION:

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

