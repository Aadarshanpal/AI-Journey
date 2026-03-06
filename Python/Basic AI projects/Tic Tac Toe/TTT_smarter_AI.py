"""
This AI might be smarter but its still at the level of "If i can win, i will" and "If i can stop you from winning i will".
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

    while True:
        index = random.randint(0,len(board)-1)

        if board[index] == '-':
            board[index] = 'X'
            break

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
        if turn_buffer == 'X':
            print("You might just be a horrible player :(")
        break

    if draw_check(board):
        print("------------------------------------------------------------")
        draw_board(board)
        print("The game is a draw.")
        break

    print("------------------------------------------------------------")

print("------------------------------------------------------------")