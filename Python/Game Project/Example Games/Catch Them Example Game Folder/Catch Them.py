# imports 
import pygame
import random
import time
import math

# cat falling objects class
class Pet:
    def __init__(self):
        self.name = random.choice(['cloud','cat','cat','cat','cat']) # randomly generates what object they are 
        
        if self.name == 'cloud':
            self.x = random.randint(0,3000)
            self.y = random.randint(50,200)
            self.size = random.randint(50,100)
            self.falling = False
        if self.name == 'cat': # cats start far above the screen so they "fall"
            self.x = random.randint(50,1350)
            self.x = self.x // 5 * 5
            self.y = random.randint(-5000,-100)
            self.size = 30

            
            if random.randint(1,10) == 2:
                self.size = 60
            self.falling = True
            
        self.caught = False
        self.image = pygame.image.load('image/'+self.name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.size,self.size)) # loads the image based on the object 
        self.speed = random.randint(1,3)
        self.target = False
        

    def do(self,surface,player): # this causes the object to move, clouds move right to left while cats move down to the bottom
        surface.blit(self.image,(int(self.x),self.y))
        if self.name == 'cloud':
            self.x -= 1
            if self.x < -200:
                self.x = random.randint(1400,3000)
                self.y = random.randint(50,200)
        else:
            
            if self.y < 670: # cats have a sensor at the bottom of them for when they hit the bottom of the screen they stop falling 
                self.y += self.speed
                if self.y > 500 and self.y < 665:
                    if surface.get_at((self.x,self.y+2)) not in [(173, 216, 230, 255),(0, 255, 0, 255),(253, 253, 253, 255)]:
                        self.caught = True
            elif self.y >= 670 and self.x > 50 and self.x < 1350:
                self.hit_points(surface)
                if self.size == 60:
                    self.image = pygame.transform.scale(self.image,(30,30))
            else:
                self.falling = False
                if self.size == 60:
                    self.image = pygame.transform.scale(self.image,(30,30))
        if self.target:
            pygame.draw.rect(surface,'red', pygame.Rect(self.x,self.y,self.size,self.size),1)

    def hit_points(self,surface): # cats have hit points on their left and right sides this allows them to be pushed away by the player 
        right = (self.x+40,self.y+5)
        left = (self.x-10,self.y+5)
        if surface.get_at(right) not in [(173, 216, 230, 255),(0, 255, 0, 255),(253, 253, 253, 255)]:
            self.x -= 1
        elif surface.get_at(left) not in [(173, 216, 230, 255),(0, 255, 0, 255),(253, 253, 253, 255)]:
            self.x += 1
        right = (self.x+45,self.y+5)
        left = (self.x-15,self.y+5)
        if surface.get_at(right) not in [(173, 216, 230, 255),(0, 255, 0, 255),(253, 253, 253, 255)]:
            self.x -= 1
        elif surface.get_at(left) not in [(173, 216, 230, 255),(0, 255, 0, 255),(253, 253, 253, 255)]:
            self.x += 1
        
# this is our player class 
class Player:
    def __init__(self):
        self.x = 650
        self.y = 600
        self.direction = '0'
        self.big = 0
    def draw(self,surface):
        self.image = pygame.image.load("image/basket"+self.direction+".png").convert_alpha() # draws our player the self.direction is used to determine which way to face
        if self.big == 0:
            self.image = pygame.transform.scale(self.image,(100,100))
            surface.blit(self.image,(self.x,self.y))
        else:
            self.image = pygame.transform.scale(self.image,(200,200))
            self.big -= 1
            if self.big > 900: # this is used when the player levels up and catches a larger pet 
                for i in range(50):
                    x = random.randint(-10,210)
                    y = random.randint(-100,-10)
                    pygame.draw.rect(surface,'yellow', pygame.Rect(self.x+x,self.y+y-50,3,3))
            surface.blit(self.image,(self.x,self.y-100))
            if self.big > 0 and self.big < 200 and random.choice([True,False,False,False]):
                pygame.draw.rect(surface,'red', pygame.Rect(self.x+75,self.y,50,50))

    def distance(self,obj): # check the distance between an object and the player
        A = abs(self.x - obj.x)
        B = abs(self.y - obj.y)
        C = A*A + B*B
        
        return math.sqrt(C)
    def move(self,surface,objects,mode=None):
        self.draw(surface)
        if mode == 'Ai': # the AI searches for the closest cat and trys to catch it before it hits the bottom of the screen 
            temp = []
            for o in objects:
                if o.name != 'cloud':
                    temp.append(o)
            # get the lowest cat
            lowest = temp[0]
            for obj in temp:
                obj.target = False
                if self.distance(obj) < self.distance(lowest) and obj.y < 650:
                    lowest = obj
            if self.x+50 < lowest.x:
                self.direction = '2'
            elif self.x+50 > lowest.x:
                self.direction = '1'
            else:
                self.direction = '0'
            if lowest.name != 'cloud':
                lowest.target = True
        
        # this uses the bottons of the keyboard
        if self.direction == '1' and self.x > 5:
            self.x -= 5
        if self.direction == '2' and self.x < 1300:
            self.x += 5
         
        
# gaming function which is used to actually play the game 
def game(surface,pets):
    RUN = True
    font = pygame.font.Font('freesansbold.ttf', 40) # create our font size for our buttons
    PLAYER = Player()
    AI = Player() # AI player only used in the begining 
    TOTAL = 0
    while RUN:
        time.sleep(.01) # frames per second 
        # draw sky
        pygame.draw.rect(surface,'light blue', pygame.Rect(0,0,1400,500))
        # draw grass
        pygame.draw.rect(surface,(0,255,0), pygame.Rect(0,500,1400,200))

        PLAYER.move(surface,pets)
        DONE = True
        for pet in pets:
            pet.do(surface,PLAYER)
            if pet.caught: # when the cat is caught the score goes up 
                pets.remove(pet)
                TOTAL += 1
                if pet.size == 60:
                    PLAYER.big = 1000
            if pet.y < 665 and pet.name != 'cloud':
                DONE = False
            
        if DONE: # when game is over the score is saved to the text file 
            file = open("high_score.txt",'r')
            score = int(file.readline())
            file.close()
            if TOTAL > score:
                file = open("high_score.txt",'w')
                file.write(str(TOTAL))
                file.close()
            menu(surface,[Pet() for i in range(100)],"Game Over")
        
        #draw display
        text = font.render(f"TOTAL: {TOTAL}", True, 'black')
        surface.blit(text , (550,10))
        x,y = pygame.mouse.get_pos() # get where the mouse pos is currently
        

        # iterate over each event to check if a button was clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    
                    menu(surface,[Pet() for i in range(100)],"Game Over")
                if event.key == pygame.K_RIGHT:
                    PLAYER.direction = '2'
                if event.key == pygame.K_LEFT:
                    PLAYER.direction = '1'
            if event.type == pygame.KEYUP:
                PLAYER.direction = '0'
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(surface.get_at((x,y)))
                if x > 625 and x < 775 and y > 300 and y < 350: # run the game
                    game(surface,pets) # pass the surface and stars
                if x > 625 and x < 775 and y > 400 and y < 450: # end the game
                    RUN = False
        pygame.display.flip()
        
    #pygame.quit() # this closes the pygame window

def menu(surface,pets,display): # menu function 
    RUN = True
    font = pygame.font.Font('freesansbold.ttf', 40) # create our font size for our buttons
    PLAYER = Player()
    file = open("high_score.txt",'r')
    score = int(file.readline())
    file.close()
    while RUN:
        time.sleep(.01)
        # draw sky
        pygame.draw.rect(surface,'light blue', pygame.Rect(0,0,1400,500))
        # draw grass
        pygame.draw.rect(surface,(0,255,0), pygame.Rect(0,500,1400,200))

        PLAYER.move(surface,pets,'Ai') # the game plays auto version 
        
        for pet in pets: # move the cats downwards 
            pet.do(surface,PLAYER)
            if pet.caught:
                pet.caught = False
                pet.y = random.randint(-5000,-100)
                if pet.size == 60:
                    PLAYER.big = 1000
            if pet.y > 665:
                pet.x = random.randint(50,1350)
                pet.x = pet.x // 5 * 5
                pet.y = random.randint(-5000,-100)
            
        
        
        #draw display
        text = font.render(f"{display}", True, 'black')
        surface.blit(text , (550,150))
        text = font.render(f"HIGH SCORE: {score}", True, 'black')
        surface.blit(text , (550,200))
        x,y = pygame.mouse.get_pos() # get where the mouse pos is currently
        
        # check if mouse pos is in range of our start button
        if x > 625 and x < 775 and y > 300 and y < 350:
            start_button_color = 'dark blue'
        else:
            start_button_color = 'blue'
        # draw our start button
        pygame.draw.rect(surface,start_button_color, pygame.Rect(625,300,150,50))
        text = font.render("START", True, 'white')
        surface.blit(text , (630,305))

        # check if mouse pos is in range of our exit button
        if x > 625 and x < 775 and y > 400 and y < 450:
            end_button_color = 'dark blue'
        else:
            end_button_color = 'blue'
        # draw our end button
        pygame.draw.rect(surface,end_button_color, pygame.Rect(625,400,150,50))
        text = font.render("EXIT", True, 'white')
        surface.blit(text , (645,405))

        # iterate over each event to check if a button was clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x > 625 and x < 775 and y > 300 and y < 350: # run the game
                    game(surface,[Pet() for i in range(100)]) # pass the surface and stars
                if x > 625 and x < 775 and y > 400 and y < 450: # end the game
                    RUN = False
                
        pygame.display.flip()
    pygame.quit() # this closes the pygame window
    

def main():
    pygame.init()
    surface = pygame.display.set_mode((1400,700)) # create pygame window and screen
    pygame.display.set_caption('Catch Them!') # sets title
    pets = [Pet() for i in range(100)] # get the 100 pet objects 
    menu(surface,pets,"Catch Them!") # calls the menu 


main() # call to main
