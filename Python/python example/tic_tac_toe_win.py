def check_win(board,player):
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    if board[0] == board[1] and board[1] == board[2] and board[2] == player:
        print(player,"WINS!")
        return True
    if board[3] == board[4] and board[4] == board[5] and board[5] == player:
        print(player,"WINS!")
        return True
    if board[6] == board[7] and board[7] == board[8] and board[8] == player:
        print(player,"WINS!")
        return True
    if board[0] == board[3] and board[3] == board[6] and board[6] == player:
        print(player,"WINS!")
        return True
    if board[1] == board[4] and board[4] == board[7] and board[7] == player:
        print(player,"WINS!")
        return True
    if board[2] == board[5] and board[5] == board[8] and board[8] == player:
        print(player,"WINS!")
        return True
    if board[0] == board[4] and board[4] == board[8] and board[8] == player:
        print(player,"WINS!")
        return True
    if board[2] == board[4] and board[4] == board[6] and board[6] == player:
        print(player,"WINS!")
        return True

    # check if it is a tie
    tie = True
    for spot in board:
        if spot != 'X' and spot != 'O':
            tie = False

    if tie:
        print('Its a tie!')
        return True
    
    return False
