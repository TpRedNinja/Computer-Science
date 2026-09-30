import pygame
import random
import math

class Car():
    def __init__(self):
        self.color = random.choice(['red','blue','black'])
        self.direction = random.choice('NESW')
        self.at_red_light = False
        self.ignore = 0
        self.turn = 0
        self.balance = 0
        if self.direction == 'N':
            self.y = random.randint(800,1500)
            self.x = 0
        if self.direction == 'S':
            self.y = random.randint(-1000,-100)
            self.x = 0
        if self.direction == 'E':
            self.x = random.randint(-1000,-100)
            self.y = 0
        if self.direction == 'W':
            self.x = random.randint(800,1500)
            self.y = 0
        
    def draw(self,window):
        if self.direction == 'N':
            pygame.draw.rect(window, self.color, [self.x, self.y, 20, 50])
        elif self.direction == 'S':
            pygame.draw.rect(window, self.color, [self.x, self.y, 20, 50])
        elif self.direction == 'E':
            pygame.draw.rect(window, self.color, [self.x, self.y, 50, 20])
        elif self.direction == 'W':
            pygame.draw.rect(window, self.color, [self.x, self.y, 50, 20])
    def drive(self,window):
        if self.balance == 0:
            speed = 1
        else:
            speed = 0
            
        if self.turn == 150:
            self.direction = random.choice('NESW')

        if self.turn > 0:
            self.turn -= speed
            
        if self.direction == 'N':
            self.y -= speed
            self.x = 355 + self.balance
        elif self.direction == 'S':
            self.y += speed
            self.x = 325 - self.balance
        elif self.direction == 'E':
            self.x += speed
            self.y = 355 + self.balance
        elif self.direction == 'W':
            self.x -= speed
            self.y = 325 - self.balance
        if self.x < -1000 or self.x > 1500 or self.y < -1000 or self.y > 1500:
            self.reset()

    def check(self,window):
        if self.ignore != 0:
            self.ignore -= 1
        try:
            CARS = [(255,0,0,255),(0,0,255,255),(0,0,0,255)]
            if self.direction == 'N' and window.get_at((self.x+5,self.y-15)) not in CARS:
                return True
            elif self.direction == 'S' and window.get_at((self.x+5,self.y+65)) not in CARS:
                return True
            elif self.direction == 'W' and window.get_at((self.x-15,self.y+5)) not in CARS:
                return True
            elif self.direction == 'E' and window.get_at((self.x+65,self.y+5)) not in CARS:
                return True
            else:
                return False
        except:
            return True
            
    def reset(self):
        self.direction = random.choice('NESW')
        if self.direction == 'N':
            self.y = random.randint(800,1500)
            self.x = 0
        if self.direction == 'S':
            self.y = random.randint(-1000,-100)
            self.x = 0
        if self.direction == 'E':
            self.x = random.randint(-1000,-100)
            self.y = 0
        if self.direction == 'W':
            self.x = random.randint(800,1500)
            self.y = 0
    def balance_me(self):
        if self.balance == 0:
            speed = 1
        else:
            speed = 0
            
        if self.direction == 'N':
            self.x = 355 + self.balance
        elif self.direction == 'S':
            self.x = 325 - self.balance
        elif self.direction == 'E':
            self.y = 355 + self.balance
        elif self.direction == 'W':
            self.y = 325 - self.balance
        if self.x < -1000 or self.x > 1500 or self.y < -1000 or self.y > 1500:
            self.reset()

class Ambulance(Car):
    def __init__(self,car_list):
        Car.__init__(self)
        self.color = 'white'
        self.car_list = [c for c in car_list]
    def near(self,obj):
        A = (self.x+15) - (obj.x+15)
        B = (self.y+15) - (obj.y+15)
        C = math.sqrt(A*A + B*B)
        if C < 250:
            return True
        return False
    def drive(self,window):
        self.at_red_light = False
        for car in self.car_list:
            if self.near(car):
                car.balance = 20
            else:
                car.balance = 0
        Car.drive(self,window)
        

