class Police:
    def __init__(self,vision,health,dmg,speed):
        self.vision = vision
        self.health = health
        self.dmg = dmg
        self.speed = speed

    def get_vision(self):
        return self.vision
        
    def get_health(self):
        return self.health
        
    def get_dmg(self):
        return self.dmg
        
    def get_speed(self):
        return self.speed

    def set_vision(self,vision):
        self.vision = vision

    def set_health(self,health):
        self.health = health

    def set_dmg(self,dmg):
        self.dmg = dmg

    def set_speed(self,speed):
        self.speed = speed
