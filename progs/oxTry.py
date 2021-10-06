from random import randrange
# identify empty tiles
def findEmptyTiles(board):
    emptyTiles = [] # create placeholder list of tuples
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                emptyTiles.append((row,col)) #add tuple to list with index of empty tile
    return emptyTiles

#print values in tiles, row by row
def showBoard(board):
    for r in range(3):
        print("+-------"*3, "+", sep="")
        print("|       "*3, "|", sep="")
        for c in range(3):
            print("|  ", board[r][c], " ", sep=" ", end=" ")
        print("|")
        print("|       "*3, "|", sep="")
    print("+-------"*3, sep=" ")

def computerMove(board):
    emptyTiles = findEmptyTiles(board)
    if len(emptyTiles) > 0:
        print("My Turn")
        tile = randrange(len(emptyTiles)) # pick random num from range of empty tiles
        row, col = emptyTiles[tile] # unpack empty tile tuple into row and col
        board[row][col] = "X" # assign X to selected tile
        
def userMove(board):
    endOfTurn = False
    while not endOfTurn:
        move = int(input("make your move: "))
        if(move > 9 or move < 1):
            print("Look at the board: pick a number")
            continue
        row = (move-1) // 3
        col = (move-1) % 3
        if board[row][col] in ['O','X']:
            print("LOOK AT THE BOARD, DOOFUS!")
            continue
        else:
            endOfTurn=True
    board[row][col] = 'O'

def checkForWinner(board):
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
            winner = board[1][1]
    if board[0][2] == board[1][1] == board[2][0]: 
            winner = board[1][1]
    return winner
            

#create empty board with numbered tiles 1-9 (start top left across then down)
board = [[(i+1)+(3*j) for i in range(3)] for j in range(3)]
emptyTiles = findEmptyTiles(board)
usersTurn = True

while len(findEmptyTiles(board)):
    showBoard(board)
    if usersTurn:
        userMove(board)
    else:
        computerMove(board)
    winner = checkForWinner(board)
    if winner != None:
        if winner == "X":
            print("You Lost. Better Luck next time")
        else:
            print("Congratulations, you won!")
        break
    usersTurn = not usersTurn
    emptyTiles = findEmptyTiles(board)    

showBoard(board)
