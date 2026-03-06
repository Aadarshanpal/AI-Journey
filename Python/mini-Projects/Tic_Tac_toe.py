board = ['-','-','-',
         '-','-','-',
         '-','-','-']


turn = 'O'
game_over = False


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

while not game_over:
    draw_board(board)

    turn = take_input(turn,board)
    #check if someone has won
    if draw_check(board):
        draw_board(board)
        print("The game is a draw.")
        break

    print("---------------------------------------------------------------\n\n\n")