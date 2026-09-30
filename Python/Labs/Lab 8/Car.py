
class Vehicle:
    def __init__(self,color,x,y,speed,length,width,direction):
        self.__color = color
        self.__xCord = x
        self.__yCord = y
        self.__speed = speed
        self.__length = length
        self.__width = width
        self.__direction = direction

    def get_color(self):
        return self.__color

    def get_xCord(self):
        return self.__xCord

    def get_yCord(self):
        return self.__yCord

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_direction(self):
        return self.__direction

    def get_speed(self):
        return self.__speed

    def set_color(self,color):
        self.__color = color

    def set_xCord(self,x):
        self.__xCord = x

    def set_yCord(self,y):
        self.__yCord = y

    def set_length(self,length):
        self.__length = length

    def set_width(self,width):
        self.__width = width

    def set_direction(self,direction):
        self.__direction = direction

    def set_speed(self,speed):
        self.__speed = speed

    def drive(self):
        if self.__direction == 'south':
            self.__yCord += 1
        elif self.__direction == 'north':
            self.__yCord -= 1
        elif self.__direction == 'east':
            self.__xCord += 1
        elif self.__direction == 'west':
            self.__xCord -= 1
        elif self.__direction == 'stop':
            pass

    def __str__(self):
        return f"The cars current position is ({self.__xCord},{self.__yCord} and is heading {self.__direction}"

class PoliceCar(Vehicle):
    def __init__(self,color,x,y,speed,length,width,direction,lightsOn,chaseObject,isPolice):
        Vehicle.__init__(self,color,x,y,speed,length,width,direction)
        self.__lightsOn = lightsOn
        self.__chaseObject = chaseObject
        self.__isPolice = isPolice

    def  get_lightsOn(self):
        return self.__lightsOn

    def  get_chaseObject(self):
        return self.__chaseObject

    def  get_isPolice(self):
        return self.__isPolice

    def  set_lightsOn(self,lightsOn):
        self.__lightsOn = lightsOn

    def  set_chaseObject(self,chaseObject):
        self.__chaseObject = chaseObject

    def  set_isPolice(self,isPolice):
        self.__isPolice = isPolice
    
