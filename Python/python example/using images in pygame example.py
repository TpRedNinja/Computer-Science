# import pygame
import pygame
import time

pygame.init()

# caption/ title function
surface = pygame.display.set_mode((500,500))


pygame.display.set_caption("baseball")

#create image of ball
image = pygame.image.load("baseball.png").convert()

image = pygame.transform.scale(image,(100,100))
#variables
X = 250
Y = 250
bounce = False
GRAB = False
RUN = True

while RUN:
    pos = pygame.mouse.get_pos()
    surface.fill("white")
    surface.blit(image, (X,Y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if surface.get_at(pos)!= (255,255,255,255): 
                GRAB = True
                bounce = False
        if event.type == pygame.MOUSEBUTTONUP:
            GRAB = False
        
    # either move ball up or down.
    if bounce:
        Y -= .5
        if Y <= 0:
            bounce = False
    else:
        Y += .5
        if Y >= 450:
            bounce  = True

    if GRAB:
        X = pos[0]- 75
        Y = pos[1]- 75

    
    time.sleep(1/1000)


    # use a while loop and make the ball move
    pygame.display.flip()
