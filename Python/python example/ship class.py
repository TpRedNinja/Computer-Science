class Ship:
    def __init__(self,name,length, width, height, max_weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.max_weight = max_weight
        self.__speed = 0
        self.latitude = 40.7
        self.longitude = -74.0
        self.direction = 'N'
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed = speed
        
    def move(self):
        if 'N' in self.direction:
            self.latitude += self.speed
        if 'E' in self.direction:
            self.longitude += self.speed
        if 'S' in self.direction:
            self.latitude -= self.speed
        if 'W' in self.direction:
            self.longitude -= self.speed
        
    def steer(self,right_or_left):
        key = ['N','NE','E','SE','S','SW','W','NW']
        index = key.index(self.direction)
        if right_or_left == 'right':
            if index + 1 == len(key):
                self.direction = key[0]
            else:
                self.direction = key[index+1]
            
        if right_or_left == 'left':
            self.direction = key[index-1]
        
    def __str__(self):
        return f"The SS.{self.name} Direction: {self.direction}\nLength: {self.length}ft.\nWidth: {self.width}ft.\nHeight: {self.height}ft.\nMax Load: {self.max_weight}"

class Cargo_Ship(Ship):
    def __str__(self):
        return 'Cargo ship info:\n' +Ship.__str__(self) + f"\nDestination: {self.go_to}"
        
    def __init__(self,name,length, width, height, max_weight,go_to):
        Ship.__init__(self,name,length, width, height, max_weight)
        self.go_to = go_to
def main():
    myShip = Ship('Frock',230,30,20,1000)
    print(myShip)
    myShip2 = Cargo_Ship('Frock',230,30,20,1000,'New orleans')
    print(myShip2)


main()
