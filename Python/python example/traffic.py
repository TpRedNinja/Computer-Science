# Importing pygame module
import pygame
import random
from pygame.locals import *
import traffic_car
import math
import time
class Intersection:
    def __init__(self):
        self.timer = 0
        self.direction = random.choice('NSEW')
    def control(self,cars):
        self.timer += 1
        if self.timer == 500:
            self.timer = 0
            self.direction = random.choice('NSEW')

        for car in cars:
            if self.in_range((car.x+10,car.y+10),90):
                car.ignore = 100
            if self.in_range((car.x+10,car.y+10),40) and car.turn == 0:
                car.turn = 150
            if car.direction != self.direction and self.in_range((car.x+10,car.y+10),100):
                car.at_red_light = True
            else:
                car.at_red_light = False

    def in_range(self,pos,value):
        A = 350 - pos[0]
        B = 350 - pos[1]
        C = math.sqrt(A*A + B*B)
        if C < value:
            return True
        else:
            return False
        
            
pygame.init()
window = pygame.display.set_mode((700, 700))

RUN = True
CARS = [traffic_car.Car() for i in range(10)]
temp_car = traffic_car.Ambulance(CARS)
CARS.append(temp_car)

my_intersection = Intersection() # create out intersection object
while RUN:
    time.sleep(.001)
    # draw road
    window.fill("green")
    pygame.draw.rect(window, "grey", [300, 0, 100, 900])
    pygame.draw.rect(window, "white", [380, 0, 10, 900])
    pygame.draw.rect(window, "white", [310, 0, 10, 900])
    pygame.draw.rect(window, "grey", [0, 300, 900, 100])
    pygame.draw.rect(window, "white", [0, 380, 900, 10])
    pygame.draw.rect(window, "white", [0, 310, 9000, 10])
    pygame.draw.rect(window, "grey", [300, 300, 100, 100])
    
    for event in pygame.event.get():
        if event.type == QUIT:
            RUN = False

    my_intersection.control(CARS) # allow the intersection to control the traffic
    
    for car in CARS:
        car.draw(window)

    for car in CARS:
        car.balance_me()
        if car.check(window) and (not car.at_red_light or car.ignore != 0):
            car.drive(window)
        
    pygame.display.update()
pygame.quit()
