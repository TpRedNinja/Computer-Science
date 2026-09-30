import pygame
import drive
pygame.init()
surface = pygame.display.set_mode((700,600))
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
track = (82,77,80)
green = (0, 255, 0)
black = (0,0,0)
x= 30
y =30
x1 = 30
y1 = 230
x2 = 30
y2 = 430
speed = 0
car_Width = 8
car_Length = 15
direction = "south"
direction1 = "south"
direction2 = "south"
run = True
        
while run:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                if speed <= 4:
                    speed *= 2
            if event.key == pygame.K_b:
                if speed >=.5:
                    speed /= 2

            if event.key == pygame.K_s:
                if speed == 0:
                    speed = .5
                else:
                    speed = 0
                
    surface.fill(green)
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render(f'Press "s" to Start/Stop', True, black)
    textRect = text.get_rect()
    textRect.center = (700 // 2, 500 // 2)
    surface.blit(text, textRect)

    text = font.render(f'Press "g" to Speed Up Press "b" to Slow Down', True, black)
    textRect = text.get_rect()
    textRect.center = (700 // 2, 700 // 2)
    surface.blit(text, textRect)

    text = font.render(f'Speed: {speed * 10:.0f}MPH', True, black)
    textRect = text.get_rect()
    textRect.center = (700 // 2, 600 // 2)
    surface.blit(text, textRect)
    
    pygame.draw.rect(surface, track, pygame.Rect(25, 25, 30, 550)) #South Track
    pygame.draw.rect(surface, track, pygame.Rect(25, 550, 655, 30))
    pygame.draw.rect(surface, track, pygame.Rect(25, 25, 650, 30))
    pygame.draw.rect(surface, track, pygame.Rect(650, 25, 30, 550)) 

    direction = drive.steering(x,y,direction)
    
    if direction == "north" or direction == "south":
        pygame.draw.rect(surface, red, pygame.Rect(x, y, car_Width, car_Length ))
        if direction == "north":
            y -= speed

        else: 
            y += speed
    else:
        pygame.draw.rect(surface, red, pygame.Rect(x, y, car_Length , car_Width))
        if direction == "west":
            x -= speed

        else: 
            x += speed

    direction1 = drive.steering(x1,y1,direction1)
    
    if direction1 == "north" or direction1 == "south":
        pygame.draw.rect(surface, yellow, pygame.Rect(x1, y1, car_Width, car_Length ))
        if direction1 == "north":
            y1 -= speed

        else: 
            y1 += speed
    else:
        pygame.draw.rect(surface, yellow, pygame.Rect(x1, y1, car_Length , car_Width))
        if direction1 == "west":
            x1 -= speed

        else: 
            x1 += speed

    direction2 = drive.steering(x2,y2,direction2)
    
    if direction2 == "north" or direction2 == "south":
        pygame.draw.rect(surface, blue, pygame.Rect(x2, y2, car_Width, car_Length ))
        if direction2 == "north":
            y2 -= speed

        else: 
            y2 += speed
    else:
        pygame.draw.rect(surface, blue, pygame.Rect(x2, y2, car_Length , car_Width))
        if direction2 == "west":
            x2 -= speed

        else: 
            x2 += speed
            
    pygame.display.flip()
        
