import random
import time
import pygame

# class block which is used to display each corn block
class Block():
    def __init__(self):
        self.name = 'corn'
        image = pygame.image.load('image/'+self.name+'.png').convert_alpha()
        self.image = pygame.transform.scale(image,(60,60)) # we store about create our image here to help with speed 
        if self.name == 'path':
            self.image = pygame.transform.rotate(self.image,random.choice([0,90,180,270]))
        self.has_gas = False
        if random.randint(1,100) == 50: # their is a 2% chance that this block will have a gas tank 
            self.has_gas = True
            
    def display(self,surface,pos):
        surface.blit(self.image,pos)
        if self.has_gas:
            image = pygame.image.load('image/gas.png').convert_alpha()
            image = pygame.transform.scale(image,(60,60))
            surface.blit(image,pos) # display the image of the corn
    def dirt(self): # this function changes the image when the tractor mows over it 
        if self.name != 'path':
            self.name = 'path'
            image = pygame.image.load('image/path.png').convert_alpha()
            self.image = pygame.transform.scale(image,(60,60)) # new image 
            if self.name == 'path':
                self.image = pygame.transform.rotate(self.image,random.choice([0,90,180,270]))

# create our tractor class
class Tractor():
    def __init__(self):
        self.name = 'tractor'
        image = pygame.image.load('image/tractor.png').convert_alpha()
        self.image = pygame.transform.scale(image,(60,60)) # we store about create our image here to help with speed 
        self.x = 0
        self.y = 0
        self.past = (0,0)
        self.rotation = 0
        self.go_to = (0,0,1)
        self.movement = 0
        self.gas = 2000 # tractor gas level
        self.count = 0
    def display(self,surface):
        surface.blit(self.image,(self.x,self.y)) #image display
        
    def go_here(self,pos): # this function makes the tractor move to a certain location based on the locations x and y points and the tractors 
        pos = (pos[0]//60*60,pos[1]//60*60,random.randint(1,4))
        self.go_to = (pos[0],pos[1],1)
        self.count += 1
        
    def rotate(self,num): # this rotates the tractor 
        if self.rotate != num:
            image = pygame.image.load('image/tractor.png').convert_alpha()
            self.image = pygame.transform.scale(image,(60,60))
            self.image = pygame.transform.rotate(self.image,num)
            self.rotation = num
            
    def drive(self,field,auto=None): # drive function either move the tractor up, down, left or right. 
        if self.gas > 0:
            if auto == 'ai' and self.x == self.go_to[0] and self.y == self.go_to[1]:
                self.go_here((random.randint(5,1435),random.randint(5,715)))
                while field[self.go_to[1]// 60][self.go_to[0] // 60].name == 'path':
                    self.go_here((random.randint(5,1435),random.randint(5,715)))
            if self.go_to[2] == 1:
                if self.x < self.go_to[0]:
                    self.x += 5
                    self.rotate(-90)
                elif self.x > self.go_to[0]:
                    self.x -= 5
                    self.rotate(90)
                elif self.y < self.go_to[1]:
                    self.y += 5
                    self.rotate(180)
                elif self.y > self.go_to[1]:
                    self.y -= 5
                    self.rotate(0)
            elif self.go_to[2] == 2:
                if self.x > self.go_to[0]:
                    self.x -= 5
                    self.rotate(90)
                elif self.y < self.go_to[1]:
                    self.y += 5
                    self.rotate(180)
                elif self.y > self.go_to[1]:
                    self.y -= 5
                    self.rotate(0)
                elif self.x < self.go_to[0]:
                    self.x += 5
                    self.rotate(-90)
            elif self.go_to[2] == 3:
                if self.y < self.go_to[1]:
                    self.y += 5
                    self.rotate(180)
                elif self.y > self.go_to[1]:
                    self.y -= 5
                    self.rotate(0)
                elif self.x < self.go_to[0]:
                    self.x += 5
                    self.rotate(-90)
                elif self.x > self.go_to[0]:
                    self.x -= 5
                    self.rotate(90)
            else:
                if self.y > self.go_to[1]:
                    self.y -= 5
                    self.rotate(0)
                elif self.x < self.go_to[0]:
                    self.x += 5
                    self.rotate(-90)
                elif self.x > self.go_to[0]:
                    self.x -= 5
                    self.rotate(90)
                elif self.y < self.go_to[1]:
                    self.y += 5
                    self.rotate(180)
    
            
        X = self.x // 60
        Y = self.y // 60
        if X >= 0 and X < 24 and Y >= 0 and Y < 12:
            field[Y][X].dirt()
            if field[Y][X].has_gas:
                field[Y][X].has_gas = False
                self.gas += 1000
        if self.past != (self.x,self.y):
            self.gas -= 1
            self.past = (self.x,self.y)

        
def main():      
    pygame.init()
    surface = pygame.display.set_mode((1440,760)) # create our pygame window
    RUN = True

    FIELD = [[Block() for i in range(24)] for j in range(12)]
    TRACTOR = Tractor()
    COUNT = 0
    while RUN:
        #time.sleep(.01)
        x,y = pygame.mouse.get_pos() # gets the mouse pos
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN: # executes when the mouse button is pressed 
                TRACTOR.go_here((x,y))
                COUNT += 1

        surface.fill('black') # fills the background with this color
        i = 0
        j = 0
        WIN = True
        # loops through all the paths and checks if all of them have been mowed over. 
        for line in FIELD:
            for box in line:
                box.display(surface,(i,j))
                if box.name != 'path':
                    WIN = False
                i += 60
            j += 60
            i = 0

        if not WIN: # ends game when all the corn paths are mowed over
            TRACTOR.drive(FIELD,'')
        if WIN or TRACTOR.gas <= 0:
            print(TRACTOR.count)
            print(TRACTOR.gas)
            print()
            main()
        TRACTOR.display(surface)

        font = pygame.font.Font('freesansbold.ttf',18) # creates a font object 
        bar = ''
        for i in range(0,TRACTOR.gas,30):
            bar += '|' # concat '|' to make a bar symbol for the current gas level 
        text = font.render(f'SCORE: {TRACTOR.count} ',True,'white')
        surface.blit(text,(0,730))
        color = 'green'
        if TRACTOR.gas < 300:
            color = 'red'
        elif TRACTOR.gas < 900:
            color = 'yellow'
        text = font.render(f'FUEL: {bar}',True,color) # draws and displays the font which is the tractors score and gas level. 
        surface.blit(text,(700,730))
        
        pygame.display.update() # flips and displays the screen 
    pygame.quit() # close the pygame window
main() # call to main
