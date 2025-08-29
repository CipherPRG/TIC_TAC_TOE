# ---- Tic Tac Toe ----

# Creating the board 
board = [' '] * 9

def printboard(board):
    print(f"{board[0]}  | {board[1]} |  {board[2]}")
    print("---+---+---")
    print(f"{board[3]}  | {board[4]} |  {board[5]}")
    print("---+---+---")
    print(f"{board[6]}  | {board[7]} |  {board[8]}")


def inputboardx(board):
    p = int(input("Enter the position (0-8) for X: "))

    while p < 0 or p > 8:
        p = int(input("Enter a number between 0-8: "))
    
    while board[p] != ' ':
        p = int(input("That spot is taken, choose another: "))
    
    #As the first player is always X we place it automatically 
    board[p] = 'X'
    printboard(board)
    #this if is used to check if the person won if yes it returns true 
    if check_win(board):
        return


def inputboardo(board):
    #Taking input from the user to place on the board 
    o = int(input("Enter the position (0-8) for O: "))
    
    #To check whether the position entered is valid or not 
    while o < 0 or o > 8:
        o = int(input("Enter a number between 0-8: "))
    
    # To check if spot is taken
    while board[o] != ' ':
        o = int(input("That spot is taken, choose another: "))
    
    # Placing O directly because second player is always O
    board[o] = 'O'
    printboard(board)

    if check_win(board):
        return


def check_win(board):
    # first we check for rows for win condition
    for row in range(0, 9, 3):  
        if board[row] == board[row+1] == board[row+2] != ' ':
            print(f"{board[row]} wins!")
            return True
    #second we check for column for win condition
    for col in range(3):  
        if board[col] == board[col+3] == board[col+6] != ' ':
            print(f"{board[col]} wins!")
            return True
    #third we check for diagonal for win condition this part was a bit complex comapred to first two
    diggy = [(0, 4, 8), (2, 4, 6)]
    for d in diggy:
        if board[d[0]] == board[d[1]] == board[d[2]] != ' ':
            print(f"{board[d[0]]} wins!")
            return True
    #We check for draw condition 
    if ' ' not in board:
            print("It's a draw!")
            return True
    #we return false false so that the outside loop keeps running until win or draw
    return False

# ---- Game Loop ----
print("WELCOME TO TIC-TAC-TOE")
printboard(board)
#this loop is used to simulate the person if he has won or not 
while not check_win(board):
    inputboardx(board)
    if check_win(board):# this is done to check if the person has won midway and end the game 
        break
    inputboardo(board)
print("THANK YOU")