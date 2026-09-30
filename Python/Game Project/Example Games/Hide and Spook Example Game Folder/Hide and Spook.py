import pygame
import random

# rock object class
class Rock:
    def __init__(self):
        self.x = random.randint(-1000,2000) # randomly generates the location of the rock 
        self.y = random.randint(-1000,2000) # randomly generates the location of the rock 
        self.has_ghost = False
        
        self.has_remote = False
        self.broken = False
        self.ghost_animation = 0
        self.animation = ''
        self.rotation = random.randint(0,360)
        self.name = random.choice(['rocks','tree'])
        self.image = pygame.image.load("image/"+self.name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.image = pygame.transform.rotate(self.image,self.rotation) # saves the image object to save time 

    def broke(self):
        self.image = pygame.image.load("image/"+self.name+"2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.image = pygame.transform.rotate(self.image,self.rotation) # changes the image when the player hits it 
        
    def draw(self,surface,view): # draws the rock and tree image onto the screen
        surface.blit(self.image,(self.x-50+view[0],self.y-50+view[1]))
        if self.ghost_animation > 0:
            self.ghost_animation += 1
            imp = pygame.image.load("image/"+self.animation).convert_alpha()
            imp = pygame.transform.scale(imp,(100,100))
            surface.blit(imp,(self.x-50+view[0],self.y-50+view[1]-self.ghost_animation))
            if self.ghost_animation == 100:
                self.has_ghost = False
                self.ghost_animation = 0
    def with_in(self,obj,value,view): # checks if the player is with_in a certain range of itself 
        close_x = False
        close_y = False
        x = self.x + view[0]
        y = self.y + view[1]
        if (x - obj[0] >= 0) and (x - obj[0] < value) or (obj[0] - x >= 0) and (obj[0] - x < value):
            close_x = True
        if (y- obj[1] >= 0) and (y - obj[1] < value) or (obj[1] - y >= 0) and (obj[1] - y < value):
            close_y = True

        if close_x and close_y:
            return True
        else:
            return False

# creates our player class
class Person:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.walking = False
        self.rotation = 0
        self.view = (0,0)
        self.sense = False
        self.swing = 0
    def draw(self,surface): # draws the player object 
        if self.walking:
            num = random.randint(1,3)
        else:
            num = 1
        if self.swing > 0:
            self.swing -= 1
            num = 4
        imp = pygame.image.load("image/person"+str(num)+".png").convert_alpha()
        imp = pygame.transform.scale(imp,(100,100))
        imp = pygame.transform.rotate(imp,self.rotation)
        surface.blit(imp,(self.x-50,self.y-50))

        if self.sense:
            font = pygame.font.Font('freesansbold.ttf', 40) # create our font size for our buttons
            text = font.render("!", True, 'red')
            surface.blit(text , (self.x,self.y)) 
        self.change_view(surface)
        
        return self.view 

    def change_view(self,surface): # changes the screen view was the user walks 
        if self.x - 80 < 0:
            self.view = (self.view[0]+1,self.view[1])
            self.x += 1
        if self.x + 80 > 1400:
            self.view = (self.view[0]-1,self.view[1])
            self.x -= 1
        if self.y - 80 < 0:
            self.view = (self.view[0],self.view[1]+1)
            self.y += 1
        if self.y + 80 > 700:
            self.view = (self.view[0],self.view[1]-1)
            self.y -= 1

    def follow(self,surface,mouse_x,mouse_y): # causes the player to follow the x and y points 
        x = self.x
        y = self.y
        self.walking = True
        if self.x < mouse_x and surface.get_at((x+75,y)) == (0,255,0,255):
            self.x += 1
            self.rotation = -90
        elif self.x > mouse_x and surface.get_at((x-75,y)) == (0,255,0,255):
            self.x -= 1
            self.rotation = 90
        elif self.y < mouse_y and surface.get_at((x,y+75)) == (0,255,0,255):
            self.y += 1
            self.rotation = 180
        elif self.y > mouse_y and surface.get_at((x,y-75)) == (0,255,0,255):
            self.y -= 1
            self.rotation = 0
        else:
            self.walking = False
    def with_in(self,obj,value): # checks if the player is with_in a certain range 
        close_x = False
        close_y = False
        x = self.x - self.view[0]
        y = self.y - self.view[1]
        if (x - obj.x >= 0) and (x - obj.x < value) or (obj.x - x >= 0) and (obj.x - x < value):
            close_x = True
        if (y- obj.y >= 0) and (y - obj.y < value) or (obj.y - y >= 0) and (obj.y - y < value):
            close_y = True

        if close_x and close_y and (obj.has_ghost or obj.has_remote): #  if the player is near a ghost or a remote
            return True
        else:
            return False
     
def game(surface,rocks):
    RUN = True
    font = pygame.font.Font('freesansbold.ttf', 40) # create our font size for our buttons
    PERSON = Person()
    VIEW = (0,0)
    TOTAL_GHOSTS = 0
    HITS = 5
    rocks[0].has_remote = True
    for i in range(5):
        rocks[i+1].has_ghost = True
    RADAR = [((rock.x+1000)//40+20,(rock.y+1000)//40+20) for rock in rocks]
    REMOTE = False # when this is true the player has a radar function
    while RUN:
        # draw grass
        pygame.draw.rect(surface,"green", pygame.Rect(0,0,1400,700))
        pygame.draw.rect(surface,"black", pygame.Rect(-1050+VIEW[0],-1050+VIEW[1],3100,3100),10)
        # draw rocks
        PERSON.sense = False
        for rock in rocks:
            rock.draw(surface,VIEW)
            if PERSON.with_in(rock,300):
                PERSON.sense = True
            

        x,y = pygame.mouse.get_pos() # get where the mouse pos is currently
        PERSON.follow(surface,x,y)

        VIEW = PERSON.draw(surface)
        #draw display
        text = font.render(f"GHOSTS: {TOTAL_GHOSTS} HITS: {HITS}", True, 'white')
        surface.blit(text , (850,20))
        
        # iterate over each event to check if a button was clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.MOUSEBUTTONDOWN and not PERSON.walking:
                PERSON.swing = 50
                found= False
                for rock in rocks:
                    if rock.with_in((x,y),50,VIEW):
                        rock.broke()
                        if rock.has_ghost:
                            rock.ghost_animation = 1
                            TOTAL_GHOSTS += 1
                            found = True
                            rock.animation = 'ghost.png'
                        if rock.has_remote:
                            rock.ghost_animation = 1
                            rock.animation = 'remote.png'
                            found = True
                            REMOTE = True
                        
                if not found:
                    HITS -= 1

        if REMOTE:
            # draw radar
            pygame.draw.circle(surface,"dark green",(60,60),60)
            pygame.draw.circle(surface,"black",(60,60),60,5)
            for r in RADAR:
                pygame.draw.circle(surface,"black",(r[0],r[1]),1)
            person_spot = ((PERSON.x-VIEW[0]+1000)//40+20,(PERSON.y-VIEW[1]+1000)//40+20)
            pygame.draw.circle(surface,"red",person_spot,1)
        
        
        
        pygame.display.flip()
        if RUN:
            if TOTAL_GHOSTS == 3:
                menu(surface,get_rocks(),"You Win!")
            if HITS == 0:
                menu(surface,get_rocks(),"You Lose!")

def menu(surface,rocks,display):
    RUN = True
    font = pygame.font.Font('freesansbold.ttf', 40) # create our font size for our buttons
    while RUN:
        # draw grass
        pygame.draw.rect(surface,(0,255,0), pygame.Rect(0,0,1400,700))
        # draw rocks
        for rock in rocks:
            rock.draw(surface,(0,0))
                         
        #draw display
        text = font.render(f"{display}", True, 'white')
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
                    game(surface,rocks) # pass the surface and stars
                if x > 625 and x < 775 and y > 400 and y < 450: # end the game
                    RUN = False
        pygame.display.flip()
    pygame.quit() # this closes the pygame window
    
def overlap(x,y,rocks):
    close_range = 100
    for r in rocks:
        close_x = False
        close_y = False
        if (r.x - x >= 0 and r.x - x <= close_range) or (x - r.x >= 0 and x - r.x <= close_range):
            close_x = True
        if (r.y - y >= 0 and r.y - y <= close_range) or (y - r.y >= 0 and y - r.y <= close_range):
            close_y = True
        if close_x and close_y:
            return True
    return False

def get_rocks():
    rocks = [] # this randomly generates points where rocks "pixels" can be placed.
    for num in range(100):
        new_rock = Rock()
        while overlap(new_rock.x,new_rock.y,rocks):
            new_rock = Rock()
        rocks.append(new_rock)
    return rocks
def main():
    pygame.init()
    surface = pygame.display.set_mode((1400,700)) # creates the pygame window and screen
    pygame.display.set_caption('Rock Hiding')
    rocks = get_rocks()
    menu(surface,rocks,"Rock Hiding")
main()
