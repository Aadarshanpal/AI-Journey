board = ['-','-','-',
         '-','-','-',
         '-','-','-']


def insert_move(turn):
    index = int(input(("Enter where the move is meant to be played: ")))

    if board[index] == '-':
        board[index] = turn