import pygame
import sys
import random
class Player:
    def __init__(self, name, image_path, position, health, strength, defense, vitality):
        self.name = name
        self.health = health
        self.strength = strength
        self.position = position
        self.defense = defense
        self.vitality = vitality
        self.image= pygame.image.load(image_path)
    def draw(self, screen):
        screen.blit(self.image, self.position)
    def attack(self, other_player):
        damage = self.strength - other_player.defense
        if damage > 0:
            other_player.health -= damage
            print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was too weak to harm {other_player.name}.")
    def heal(self):
        self.health += self.vitality
        print(f"{self.name} heals for {self.vitality} health!")
    def is_alive(self):
        return self.health > 0
    def __str__(self):
        return f"Player {self.name}: Health = {self.health}, Strength = {self.strength}, Defense = {self.defense}"

class Coins:
    def __init__(self,name, image_path, position, amount):
        self.position = position
        original_image = pygame.image.load(image_path)
        WxH=(random.randint(50,100))
        new_width, new_height = (WxH,WxH)  # Example dimensions
        resized_image = pygame.transform.scale(original_image, (new_width, new_height))
        self.image = resized_image
        self.amount= amount
        self.name=name
    def draw(self, screen):
        screen.blit(self.image, self.position)
    def __str__(self):
        return f"Player {self.name}: Amount = {self.amount}, POSIITON = {self.position}"

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Player attack game")
    player1 = Player("Hero","ClassicHeroMidi.png", position=(-100, 300), health=100, strength=45, defense=8, vitality=4)
    player2 = Player("Villain","sadman.png", position=(500, 300), health=80, strength=36, defense=10, vitality=8)
    coins1= Coins("Coins","coin23.png", position=(0,0),amount=random.randint(10,100))
    coins2= Coins("Coins","money.png", position=(250,300),amount=random.randint(10,100))
    black = (0, 0, 0)
    white = (255, 255, 255)
    count=1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('Coins have spawned!')
                    print(coins1)
                    print(coins2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if count % 2 == 0:
                    print(player1)
                    print(player2)
                    player2.attack(player1)
                    player1.heal()
                    print(f"Is {player1.name} alive? {player1.is_alive()}")
                    print(f"Is {player2.name} alive? {player2.is_alive()}")
                    print(player1)
                    print(player2)
                    count+=1
                else:
                    print(player1)
                    print(player2)
                    player1.attack(player2)
                    player2.heal()
                    print(f"Is {player1.name} alive? {player1.is_alive()}")
                    print(f"Is {player2.name} alive? {player2.is_alive()}")
                    print(player1)
                    print(player2)
                    count +=1
        screen.fill(white)
        player1.draw(screen)
        player2.draw(screen)
        coins1.draw(screen)
        coins2.draw(screen)
        pygame.display.flip()
main()
# Quit Pygame
pygame.quit()
sys.exit()
