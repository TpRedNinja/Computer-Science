class Bob:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bobisgreat(self):
        print("Remember when in doubt " + self.name + " is always great")

p1 = Bob("Bob", 6)

p1.bobisgreat()

