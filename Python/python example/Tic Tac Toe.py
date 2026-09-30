# This program was made by Harris Domangue for CMSC-201 on Oct 10th 2024
# This program will create a tic tax toe game.

#player variable
player = 'O'
def intro():
    print("This program is tic tac toe")

def set_game(board,move):
    board[move-1] = player

def check_win(board):
    if board [0] == board[1] and board [1] == board [2]:
        print(player,"WINS!")
        return True
    return False

def draw_board(board):
    line = "| "
    count = 0
    for block in board:
        line += block + " | "
        count += 1
        if count == 3:
            count = 0
            print(line)
            line = "| "
def swap():
    global player
    if player == 'O':
        player = 'X'
    else:
        player = 'O'

def play():
    board = [str(i) for i in range(1,10)]
    while not check_win(board):
        draw_board(board)
        move = int(input(f'Enter where you want to play the {player}: '))
        set_game(board,move) # set to that move
        swap()

def main():
    intro()
    play()

if __name__ == '__main__':
    main()
