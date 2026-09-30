# This program was made by Justin Frock for CMSC-201 on Oct 10th
# This program will create a tic tac toe game.

import random
import tic_tac_toe_win
# player variable
player = 'O'

def intro():
    print("This is tic tac toe")

def set_game(board,move):
    # check that it is an empty space first
    if board[move-1] != 'O' and board[move-1] != 'X':
        board[move-1] = player
        return True
    else:
        return False # spot did not get placed correctly
    

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
    global player
    board = [str(i) for i in range(1,10)]
    while not tic_tac_toe_win.check_win(board,player):
        draw_board(board)
        move = int(input(f"Enter where you want to place the {player}: "))        
        if set_game(board,move): # set to that move
            swap()
    print()
    draw_board(board)

def main():
    intro()
    play()
if __name__ == '__main__':
    main()
