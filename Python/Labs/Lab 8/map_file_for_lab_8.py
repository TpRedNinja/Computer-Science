import pygame
import Car
pygame.init()
import traceback
import random
import pickle
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

path_list = []
vehicle_list = []
road_color = (115,115,115)
clickPause = 0
newCar = None

def drawgrid(w, rows, surface):
    sizebtwn = w // rows 
    for i in range(0, w, sizebtwn):
        x, y = i, i
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

class Road:
    def __init__(self,xCord,yCord):
        self.x = xCord
        self.y = yCord
        self.directions = []
        self.pastSec = 0
        self.pastCar = None

    def set_directions(self,directions):
        self.directions = directions

    def get_directions(self):
        return self.directions

    def CANmove(self,car,secs):
        if secs - self.pastSec > 15:
            return 2
        else:
            return 0
        
    def move(self,car,secs):
        try:
            chase = car.get_chaseObject()
            canChase = True 
        except:
            canChase = False
            
        if secs - self.pastSec > 15:
            self.pastCar = None
            self.pastSec = 0
        if len(self.directions) == 2 and len(self.directions) != 0:
            if car.get_direction() in self.directions:
                return car.get_direction()
            else:
                turnDirect = {"north":"south","east":"west","west":"east","south":"north"}
                tempList = self.directions
                if turnDirect[car.get_direction()] in self.directions:
                    tempList.remove(turnDirect[car.get_direction()])
                
                return random.choice(tempList)
                
                
                
        if len(self.directions) != 0 and self.pastCar != car:
            self.pastCar = car
            self.pastSec = secs
            if canChase:
                newTempList = []
                if "south" in self.directions and chase.get_yCord() > car.get_yCord():
                    newTempList.append("south")
                    
                if "north" in self.directions and car.get_yCord() > chase.get_yCord():
                    newTempList.append("north")
                    
                if "east" in self.directions and car.get_xCord() < chase.get_xCord():
                    newTempList.append("east")
                    

                if "west" in self.directions and car.get_xCord() > chase.get_xCord():
                    newTempList.append("west")
                    

                if len(newTempList) > 0:
                    return random.choice(newTempList)
                else:
                    return random.choice(self.directions)
            
            else:
                return random.choice(self.directions)
        
        else:
            return car.get_direction()
        
def getPos(x,y,sizebtwn):
        ix = x // sizebtwn
        iy = y // sizebtwn
        cx, cy = ix * sizebtwn, iy * sizebtwn
        return cx,cy

def balance(car):
    if car.get_direction() == "north":
        car.set_xCord((car.get_xCord() // 30) * 30 + 20)

    elif car.get_direction() == "east":
        car.set_yCord((car.get_yCord() // 30) * 30 + 20)

    elif car.get_direction() == "south":
        car.set_xCord((car.get_xCord() // 30) * 30 + 2)

    elif car.get_direction() == "west":
        car.set_yCord((car.get_yCord() // 30) * 30 + 2)
    
def draw(surface,sizebtwn):
    global clickPause
    click = pygame.mouse.get_pressed()
    if click[0] and clickPause == 0:
        clickPause = 1
        x, y = pygame.mouse.get_pos()
        ix = x // sizebtwn
        iy = y // sizebtwn
        cx, cy = ix * sizebtwn, iy * sizebtwn
        canPlace = True
        thisPath = None
        for p in path_list:
            if p.x == cx and p.y == cy:
                canPlace = False
                thisPath = p

        if not canPlace:
            path_list.remove(thisPath)
        else:
            square = pygame.Rect(cx, cy, sizebtwn, sizebtwn)
            pygame.draw.rect(surface, (255, 255, 255), square)

            newPath = Road(cx,cy)

            canPlace = True
            for p in path_list:
                if p.x == cx and p.y == cy:
                    canPlace = False

            if canPlace:
                path_list.append(newPath)
                    

        



run = True
canAddMore = True
secs = 0
newCar = "Use your mouse to place roads and press V to place cars"
while run:
    if clickPause > 0:
        clickPause += 1

        if clickPause == 10:
            clickPause = 0
            
    secs += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            theKey = pygame.key.name(event.key)
            if theKey == "e" or theKey == "q":
                pygame.quit()

            if theKey == "s":
                dbfile = open('Saved_Map.txt', 'ab')
                pickle.dump(path_list, dbfile)                    
                dbfile.close()

            if theKey == "a":
                try:
                    dbfile = open('Saved_Map.txt', 'rb')    
                    db = pickle.load(dbfile)
                    path_list = db
                    dbfile.close()
                except FileNotFoundError:
                    print("You don't have a Saved Map")
                    
            if theKey == "v":
                if len(path_list) < 5:
                    newCar = "You must place down more roads before pressing v"
                elif not canAddMore:
                    pass
                else:
                    canAddMore = False
                    placeOn = random.choice(path_list)
                    x = placeOn.x + 5
                    y = placeOn.y + 5
                    x1 = random.randint(1,255)
                    y1 = random.randint(1,255)
                    z1 = random.randint(1,255)
                    newCar = Car.Vehicle((x1,y1,z1),x,y,2,12,8,"east")
                    vehicle_list.append(newCar)

                    try:
                        for i in range(1,4):
                            placeOn = random.choice(path_list)
                            x = placeOn.x + 5
                            y = placeOn.y + 5
                            newCop = Car.PoliceCar((0,0,255),x,y,2,12,8,"east",True,newCar,True)
                            vehicle_list.append(newCop)
                    except:
                        print(traceback.print_exc())
                

    screen.fill((0,255,0))
    
    draw(screen, 30)
    font = pygame.font.Font('freesansbold.ttf', 18)
    text1 = font.render(str(newCar), True, (0,0,0))
    screen.blit(text1 , (50,15))

    for box in path_list:
        pygame.draw.rect(screen, road_color, pygame.Rect(box.x, box.y, 30, 30))

        if len(box.directions) == 2:
            if "east" in box.directions and "west" in box.directions:
                pygame.draw.rect(screen, (255,255,153), pygame.Rect(box.x+10, box.y+14, 10, 2))
            if "north" in box.directions and "south" in box.directions:
                pygame.draw.rect(screen, (255,255,153), pygame.Rect(box.x+14, box.y+10, 2, 10))
        
        
        newList = []
        for path in path_list:
            if "west" not in newList and path.x == box.x -30 and path.y == box.y:
                newList.append("west")
            elif "east" not in newList and path.x == box.x +30 and path.y == box.y:
                newList.append("east")
            elif "south" not in newList and path.x == box.x and path.y == box.y + 30:
                newList.append("south")
            elif "north" not in newList and path.x == box.x and path.y == box.y - 30:
                newList.append("north")

        box.set_directions(newList)

    for car in vehicle_list:
        myRoad = None
        xx = car.get_xCord()
        yy = car.get_yCord()
        color = car.get_color()
        ln = car.get_length()
        wd = car.get_width()
            
        pygame.draw.rect(screen,color, pygame.Rect(xx, yy, ln, wd))
        px, py = getPos(xx,yy,30)
        balance(car)
        car.drive()
        nextRoad = None
        try:
            car.get_isPolice()
            lightsList = [(255,0,0),(255,255,255),(0,0,255)] 
            pygame.draw.rect(screen,random.choice(lightsList), pygame.Rect(xx+4, yy+4, 3, 3))
            
        except:
            pass
            
        try:
            direct = {"north":-6,"east":18,"west":-6,"south":18}
            direct2 = {"north":-30,"east":30,"west":-30,"south":30}
            toAdd = direct[car.get_direction()]
            toAdd2 = direct2[car.get_direction()]
            if car.get_direction() == "east" or car.get_direction() == "west":
                front = screen.get_at((xx + toAdd ,yy))
                
            else:
                front = screen.get_at((xx ,yy + toAdd))

        
            if front ==(0,255,0,255):
                newDirect = {"north":"south","east":"west","west":"east","south":"north","stop":"stop"}
                car.set_direction(newDirect[car.get_direction()])
                
            elif front != (115,115,115,255):
                car.set_speed(0)

            else:
                car.set_speed(2)
                
        except Exception as e:
            print(e)
        

                
        for p in path_list:
            if p.x == px and p.y == py and myRoad == None:
                myRoad = p

        if car.get_direction() == "east" or car.get_direction() == "west":
            for p in path_list:
                if p.x == myRoad.x + toAdd2 and p.y == myRoad.y:
                    nextRoad = p

        else:
            for p in path_list:
                if p.x == myRoad.x  and p.y == myRoad.y + toAdd2:
                    nextRoad = p
        
        

        if nextRoad != None:
            car.set_speed(nextRoad.CANmove(car,secs))
        else:
            car.set_speed(2)

        if myRoad == None:
            placeOn = random.choice(path_list)
            car.set_xCord(placeOn.x + 5)
            car.set_yCord(placeOn.y + 5)

        else:
            car.set_direction(myRoad.move(car,secs))


        if car.get_direction() == "west" or car.get_direction() == "east":
            car.set_length(12)
            car.set_width(8)
            
        else:
            car.set_length(8)
            car.set_width(12)

            
                
    pygame.display.flip()
