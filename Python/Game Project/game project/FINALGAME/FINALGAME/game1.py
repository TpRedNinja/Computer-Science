import pygame
import random
import sys
# Initialize Pygame
pygame.init()
show_popup = False
def intro():
    print('press space to start')
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spacebar pressed! Perform action here.")
                    main(show_popup)
# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
GOLD = (255, 223, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
# Clock for controlling frame rate
clock = pygame.time.Clock()
# Define the Wall class
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, self.rect)
# Define the Player class
class Player:
    def __init__(self, name, image_path, position, health, strength, defense, speed, vitality, size, x, y):
        self.name = name
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_alpha(128)
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = health
        self.strength = strength
        self.defense = defense
        self.vitality = vitality
        self.speed = speed
        self.x = x
        self.y = y
        self.score = 0  # Initialize score
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def move(self, keys, walls):
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        # Calculate the potential new position
        new_rect = self.rect.move(dx, dy)
        # Check for collisions with walls
        for wall in walls:
            if new_rect.colliderect(wall.rect):
                return  # If collides with a wall, do not update the position
        # Clamp the position to ensure the player stays within the screen bounds
        new_rect.x = max(0, min(new_rect.x, screen_width - self.rect.width))
        new_rect.y = max(0, min(new_rect.y, screen_height - self.rect.height))
        # Update player position
        self.rect = new_rect
        self.x, self.y = self.rect.topleft
    def collect_coin(self, coins):
        for coin in coins[:]:
            if self.rect.colliderect(coin.rect):  # Check if player collides with coin
                self.score += coin.value  # Add coin's value to player's score
                coins.remove(coin)  # Remove the collected coin from the list
# Define the Coin class
class Coin:
    def __init__(self):
        self.image_choice = random.choice([1, 2, 3, 4, 5])  # Randomly choose an image (1, 2, or 3)
        if self.image_choice == 1:
            self.image = pygame.image.load("coins.png").convert_alpha()  # Low-value coin image
            self.image.set_alpha(128)
            self.value = random.randint(1, 10)  # Low value range
        elif self.image_choice == 2:
            self.image = pygame.image.load("diamond.png").convert_alpha()  # Medium-value coin image
            self.image.set_alpha(128)
            self.value = random.randint(30, 50)  # Medium value range
        elif self.image_choice == 3:
            self.image = pygame.image.load("gemss.png").convert_alpha()  # Medium-value coin image
            self.image.set_alpha(128)
            self.value = random.randint(50, 75)  # Medium value range
        elif self.image_choice == 4:
            self.image = pygame.image.load("chalice.png").convert_alpha()  # Medium-value coin image
            self.image.set_alpha(128)
            self.value = random.randint(50, 75)
        else:
            self.image = pygame.image.load("money.png").convert_alpha()  # High-value coin image
            self.image.set_alpha(128)
            self.value = random.randint(30, 50)  # High value range
        self.image = pygame.transform.scale(self.image, (32, 32))  # Scale image to 32x32
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)  # Random x position
        self.rect.y = random.randint(0, screen_height - self.rect.height)  # Random y position
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)  # Draw the coin image
# List of walls (same as before)
walls = [
    Wall(128, 0, 32, 32), Wall(160, 0, 32, 32),
    Wall(128, 32, 32, 32), Wall(128, 64, 32, 32),
    Wall(128, 96, 32, 32), Wall(128, 128, 32, 32),
    Wall(160, 128, 32, 32), Wall(192, 128, 32, 32),
    Wall(192, 96, 32, 32), Wall(192, 64, 32, 32),
    Wall(192, 32, 32, 32), Wall(192, 0, 32, 32),
    Wall(224, 0, 32, 32), Wall(256, 0, 32, 32),
    Wall(256, 32, 32, 32), Wall(256, 64, 32, 32),
    Wall(256, 96, 32, 32), Wall(256, 128, 32, 32),
    Wall(288, 128, 32, 32), Wall(320, 128, 32, 32),
    Wall(320, 96, 32, 32), Wall(320, 64, 32, 32),
    Wall(320, 32, 32, 32), Wall(320, 0, 32, 32),
    Wall(352, 0, 32, 32), Wall(384, 0, 32, 32),
]
# Function to draw the map
font = pygame.font.Font(None, 36)
# Player stats
player_stats = {
    "Health": 100,
    "Strength": 75,
    "Defense": 50,
    "Vitality": 90,
    "Speed": 65,
}
# Function to display the popup
def draw_stats_popup(screen, stats):
    # Popup dimensions
    popup_width, popup_height = 300, 200
    popup_x = (screen_width - popup_width) // 2
    popup_y = (screen_height - popup_height) // 2
    # Draw the popup background
    pygame.draw.rect(screen, GRAY, (popup_x, popup_y, popup_width, popup_height))
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height), 2)  # Border
    # Draw the stats text
    y_offset = 20
    for stat, value in stats.items():
        text = font.render(f"{stat}: {value}", True, WHITE)
        screen.blit(text, (popup_x + 20, popup_y + y_offset))
        y_offset += 40
def draw_map(screen):
    background_image = pygame.image.load("wood1.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    screen.blit(background_image, (0, 0))  # Draw background
    for wall in walls:
        wall.draw(screen)
#def spawn_coins(screen):
#
# Game loop function
def main(show_popup):
        running=True
        player1 = Player(
        "Hero",
        "Charmongus.png",
        position=(100, 300),
        health=100,
        strength=45,
        defense=8,
        speed=5,
        vitality=2,
        size=(32, 32),
        x=400,
        y=300,
    )
        coins=[]
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:  # Toggle popup on TAB key press
                        show_popup = not show_popup
                    elif event.key ==pygame.K_j:
                        print('j')
                        coins = [Coin() for _ in range(15)]  # Generate 10 random coins
                        print(coins)
            # Update game state
            player1.move(keys, walls)
            player1.collect_coin(coins)  # Check if player collects any coins
            # Draw everything
            draw_map(screen)
            for coin in coins:
                coin.draw(screen)
            player1.draw(screen)
            # Draw the popup if toggled
            if show_popup:
                draw_stats_popup(screen, player_stats)
            # Display the player's score
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Score: {player1.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            # Update display
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
# Run the game
if __name__ == "__main__":
    intro()
    
