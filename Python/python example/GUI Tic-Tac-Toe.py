import pygame
import tic_tac_toe_win as tttw

BOARD = ['1','2','3','4','5','6','7','8','9']
PLAYER = 'O'

def swap(player):
    if player == 'O':
        return 'X'
    else:
        return 'O'
    
def set_box(box): # This function sets the value of X and O in the board
    index = box -1
    if BOARD[index] != 'O' and BOARD[index] != 'X':
        BOARD[index] = PLAYER
        return True
    else:
        return False
def get_box(pos):
    X_value = pos[0] // 200
    Y_value = pos[1] // 200
    box = X_value + Y_value * 3 + 1 # we will talk more on this later
    return box
    
# init our screen and game
pygame.init()
# screen size
LENGTH = 600
WIDTH = 600

# function sets the screen to a width and length
SURFACE = pygame.display.set_mode((LENGTH,WIDTH)) 

RUN = True # this keeps the pygame window running
# flag to show the winner
WINNER = False
while RUN:
    pos = pygame.mouse.get_pos() # gets the position of the mouse
    SURFACE.fill("green") # fills the background with this color

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # when a user clicks on the screen
            if set_box(get_box(pos)): # noticed a nested function
                PLAYER = swap(PLAYER)

                if tttw.check_win(BOARD,PLAYER):
                    PLAYER = swap(PLAYER)
                    WINNER = True
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                RUN = False
                


    # draw a line for the board
    # the rectangle takes in its position and width and length
    index_value = 0
    for box_y in range (0,600,200):
        for box_x in range (0,600,200):
            pygame.draw.rect(SURFACE,"black",(box_x,box_y,200,200),5)

            font = pygame.font.Font('freesansbold.ttf',100)
            text = font.render(f'{BOARD[index_value]}', True, "white")
            SURFACE.blit(text, (box_x+75,box_y+50))
            
            index_value += 1
    
    # follow the curser with the player symbol
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render(f'{PLAYER}', True, "white")
    SURFACE.blit(text, pos)

    # check if someone won
    if WINNER:
        SURFACE.fill("green")
        text = font.render(f'{PLAYER} WON!', True, "white")
        SURFACE.blit(text, (200,200))
    
    # dis play the current screen
    pygame.display.flip()

pygame.quit()
