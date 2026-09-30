import pygame

pygame.init() #  init the pygame object which interacts with the sreen

screen_length = 1000
screen_width = 500
A_SET = (screen_length,screen_width)
surface = pygame.display.set_mode(A_SET)


X = 0
Y = 0
RUN = True
while RUN:
    pos = pygame.mouse.get_pos()
    surface.fill("Green") # fill the background
    color = "Red"
    # pass x y length and width
    BOX = pygame.Rect(X,Y,60,60) # this creates a rectangle object
    pygame.draw.rect(surface,color,BOX) # this sets up the rectangle for the surface

    # use a for loop and get every key movement
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if surface.get_at(pos) == (255,0,0,255):
                print("The mouse was clicked on the box!")
            else:
                print("The mouse was clciked not on the box")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Y -= 5
            if event.key == pygame.K_RIGHT:
                X += 5
            if event.key == pygame.K_LEFT:
                X -=5
            if event.key == pygame.K_DOWN:
                Y +=5
            if event.key == pygame.K_q:
                print('Program quit!')
                RUN = False

    pygame.display.flip() # displays the box on the screen
pygame.quit() # quit screen
