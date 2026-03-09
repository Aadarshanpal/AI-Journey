"""
This AI is much
"""

import random
#---------------DEFINING BOARD----------------------
board = ['-','-','-',
         '-','-','-',
         '-','-','-']
turn = 'O'


#--------------DRAWING BOARD------------------------
def draw_board(board):
    for i in range(0,len(board),3):
        print(board[i],"|",board[i+1],"|",board[i+2])


#--------------TAKING INPUT-------------------------
def take_input(board,turn):
    if turn == 'X':
        ai_input(board)
        return 'O'
    else:
        human_input(board)
        return 'X'
    

#------------------AI INPUT------------------------
def ai_input(board):
    for i in range(0,len(board)):
        if board[i] == '-':
            board[i] = 'X'
            if win_check(board):
                return

            board[i] = '-'

    for i in range(0,len(board)):
        if board[i] == '-':
            board[i] = 'O'
            if win_check(board):
                board[i] = 'X'
                return
            board[i] = '-'

    priority_list = [4,0,2,6,8]
    for i in priority_list:
        if board[i] == '-':
            board[i] = 'X'
            return    
        
    ai_depth(board)              #Creating this function because the code became too complex


    #------------------AI DEPTH (MINIMAX SIMPLE VERSION)-------------------
def ai_depth(board):

    best_score = -9999
    best_move = -1

    # Try every possible move
    for i in range(0,len(board)):

        if board[i] == '-':

            # AI plays X
            board[i] = 'X'

            score = minimax(board, 0, False)

            # Undo move
            board[i] = '-'

            if score > best_score:
                best_score = score
                best_move = i

    if best_move != -1:
        board[best_move] = 'X'


#------------------MINIMAX FUNCTION-------------------
def minimax(board, depth, is_maximizing):

    if win_check(board):

        # If AI wins
        if is_maximizing:
            return -1
        else:
            return 1

    if draw_check(board):
        return 0

    if is_maximizing:

        best_score = -9999

        for i in range(0,len(board)):

            if board[i] == '-':

                board[i] = 'X'

                score = minimax(board, depth+1, False)

                board[i] = '-'

                if score > best_score:
                    best_score = score

        return best_score

    else:

        best_score = 9999

        for i in range(0,len(board)):

            if board[i] == '-':

                board[i] = 'O'

                score = minimax(board, depth+1, True)

                board[i] = '-'

                if score < best_score:
                    best_score = score

        return best_score

#------------------HUMAN INPUT---------------------
def human_input(board):
    while True:
        try:
            index = int(input("Enter the position for your input: "))
            if 0 <= index < len(board) and board[index] == "-":
                board[index] = 'O'
                break
            else:
                print("Input a valid position.")
                continue
        except ValueError:
            print("Enter a valid position.")
            continue



#-------------CHECKING FOR WIN---------------------
def win_check(board):
    win_pattern = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for pattern in win_pattern:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != '-':
            return True
    return False




#-------------CHECKING FOR DRAW--------------------
def draw_check(board):
    for i in board:
        if i == '-':
            return False
    return True

#-------------MAIN LOOP----------------------------
while True:
    draw_board(board)

    print("------------------------------------------------------------")

    turn_buffer = turn
    turn = take_input(board,turn)

    if win_check(board):
        print("------------------------------------------------------------")
        draw_board(board)
        print("The game has been won by:",turn_buffer)
        break

    if draw_check(board):
        print("------------------------------------------------------------")
        draw_board(board)
        print("The game is a draw.")
        break

    print("------------------------------------------------------------")

print("------------------------------------------------------------")