board = ['-','-','-',
         '-','-','-',
         '-','-','-']


turn = 'O'
game_over = False


#-------------------DRAWING THE BOARD----------------------------
def draw_board(board):
    for i in range(0,8,3):
        print(board[i],"|",board[i+1],"|",board[i+2])


#-------------------CHECKING DRAW--------------------------------
def draw_check(board):
    
    for i in board:
        if i == '-':
            return False   
    return True



while not game_over:
    #fetch input and update board
    #check if someone has won
    #check if its a draw