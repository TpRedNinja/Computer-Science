#World Simulation
import pygame
import random

class Disk:
    def __init__(self,size):
        self.id = size # This is the disks id number
        self.size = 30 * size
        self.half = self.size/2-10
        self.mid = (300,size*50)
        my_colors = ['red','blue','green','orange','purple','yellow','pink']
        self.color = random.choice(my_colors) # randomly select from colors

    # displays the disk in the proper location    
    def draw(self,surface):
        pygame.draw.rect(surface,self.color, pygame.Rect(self.mid[0]-self.half,self.mid[1],self.size,20))

    # checks the color of the bottom of the disk if that color is white or black the disk is push down to the bottom    
    def down(self,surface):
        try: # we are trying to get the pixel at a certain area
            mid = (int(self.mid[0]+self.half),int(self.mid[1]+22))
            if surface.get_at(mid) == (255,255,255,255):
                self.mid = (self.mid[0],self.mid[1]+1)
            if surface.get_at(mid) == (0,0,0,255):
                self.mid = (self.mid[0],self.mid[1]+1)
            surface.set_at(mid,'red')
        except: # if the disk fell off the screen
            print("TOO MANY DISKS")
            input()

    # This converts the instructions to data points
    def move(self,where):
        where = where.split('to ')[1] # use 'to' as a token and split the instructions
        # this is use to translate the instructions to pixel values
        # peg_info = {'A':300,'B':700,'C':1100} # advanced way
        # simplier way
        if where == 'A':
            x = 300
        elif where == 'B':
            x = 700
        elif where == 'C':
            x = 1100
        # sets the peg to the new value
        self.mid = (x,200)
        
def main(DATA,num_of_disks):
    pygame.init() # init pygame object
    surface = pygame.display.set_mode((1400,500)) # set our screen
    RUN = True # set loop to intereate
    
    DISKS = [] # list to store our disks for use
    for i in range(num_of_disks,0,-1):
        DISKS.append(Disk(i)) # create our lists

    # set speed
    SPEED = 500
    index = 0-SPEED + 1
    
    while RUN:
        index += 1 # This helps us get the next set of instructions
        pygame.draw.rect(surface,(255,255,255), pygame.Rect(0,0,1500,500)) # fill background
        # gets key clicks to end program
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    RUN = False

        #draw the pegs            
        pygame.draw.rect(surface,(0,0,0), pygame.Rect(300,250,20,250))
        pygame.draw.rect(surface,(0,0,0), pygame.Rect(700,250,20,250))
        pygame.draw.rect(surface,(0,0,0), pygame.Rect(1100,250,20,250))
        #draw the floor notice the different color
        pygame.draw.rect(surface,(1,2,3), pygame.Rect(0,490,1500,10))

        # draw disks 
        for d in DISKS:
            d.draw(surface)

        # disk gravity 
        for d in DISKS:
            d.down(surface)

        # ignore this
        if index % SPEED == 0:
            if index//SPEED < len(DATA):
                go_to = DATA[index//SPEED]
                #print(go_to)
                for disk in DISKS:
                    if str(disk.id) in go_to:
                        disk.move(go_to)
        #font = pygame.font.Font('freesansbold.ttf', 18)
        #text = font.render(f"{COLORS[YY]}", True, 'black')
        #surface.blit(text , (500,500))


        pygame.display.flip() # clip screen

# This is where the program begins
# This creates an empty list
INSTRUCTIONS = []

# tower of hanoi recurssive algorithm
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        INSTRUCTIONS.append(f"disk {n} to {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    INSTRUCTIONS.append(f"disk {n} to {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)
        
# Driver code
number_of_disks = int(input('how many disks? (1-9): '))
while number_of_disks < 1 or number_of_disks > 9:
    number_of_disks = int(input('how many disks? (1-9): '))
TowerOfHanoi(number_of_disks,'A','B','C') # feed the insrtuctions to the list
main(INSTRUCTIONS,number_of_disks) # calls main and shows graphics
