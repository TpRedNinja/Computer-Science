import pygame

pygame.init() #  init the pygame object which interacts with the sreen

screen_length = 1000
screen_width = 500
A_SET = (screen_length,screen_width)
surface = pygame.display.set_mode(A_SET)

surface.fill("Green") # fill the background
color = "Red"

# pass x y length and width
BOX = pygame.Rect(30,30,60,60) # this creates a rectangle object
pygame.draw.rect(surface,color,BOX) # this sets up the rectangle for the surface

pygame.display.flip() # displays the box on the screen
