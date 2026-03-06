board = ['-','-','-',
         '-','-','-',
         '-','-','-']


turn = 'O'

print("The board is indexed from position 0 to 8, the game ends when a winning condition or draw is met.")
print("---------------------------------------------------------------\n")

#-------------------DRAWING THE BOARD----------------------------
def draw_board(board):
    for i in range(0,len(board),3):
        print(board[i],"|",board[i+1],"|",board[i+2])



#-------------------CHECKING DRAW--------------------------------
def draw_check(board):
    for i in board:
        if i == '-':
            return False   
    return True


#-------------------INPUT HANDLING-------------------------------
def take_input(turn,board):
    print("Turn:",turn)
    while True:
        try:
            index = int(input("Enter the position for your move: "))
            if 0 <= index <len(board) and board[index] == '-':
                board[index] = turn
                break
            else:
                print("That is not a valid position")
                continue
            
        except ValueError:
            print("Invalid Position please try again.\n")
            continue
    print("Move success.")
    if turn == 'O':
        return 'X'
    else:
        return 'O'


def win_check(board):
    win_patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != '-':
            return True
    
    return False

#-----------------Main game loop---------------------------
while True:
    draw_board(board)
    print("---------------------------------------------------------------")
    temp_turn = turn
    turn = take_input(turn,board)
    print("---------------------------------------------------------------")
    if win_check(board):
        draw_board(board)
        print("The Game has been won By:",temp_turn)
        break
    if draw_check(board):
        draw_board(board)
        print("The game is a draw.")
        break

    