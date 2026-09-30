import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
BROWN = (139, 69, 19)
# Clock for controlling frame rate
clock = pygame.time.Clock()

# Define the Player class
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)  # Define the wall's rectangle

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, self.rect)  # Draw the wall

# Create a list of walls
walls = [
    Wall(100, 100, 50, 200),
    Wall(300, 150, 100, 50),
    Wall(500, 200, 50, 100),
]
class Player:
    def __init__(self, name, image_path, position, health, strength, defense, speed, vitality, size, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.topleft = (x, y)  # Set the initial position of the rectangle
        self.health = health
        self.strength = strength
        self.defense = defense
        self.vitality = vitality
        self.speed = speed
        self.x = x
        self.y = y
        self.position = position
        self.rect = self.image.get_rect(topleft=(self.x, self.y))  # Get the rect for collision detection
        if size:
            self.image = pygame.transform.scale(self.image, size)
    def draw(self, screen):
        """Draw the player at its current position."""
        screen.blit(self.image, (self.x, self.y))
    def move(self, keys):
        """Move the player based on key inputs."""
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed

        # Create a new rect based on the player's current position and movement
        new_rect = self.rect.move(dx, dy)

        # Check if the new position collides with any walls
        for wall in walls:
            if new_rect.colliderect(wall.rect):  # If the player rectangle collides with a wall
                return  # Don't update the position if there's a collision
        # If no collision, update the player's position
        self.rect = new_rect
        self.x, self.y = self.rect.topleft


# Game loop function
def main():
    # Create the player
    player1 = Player(
        "Hero",
        "Coins.png",
        position=(100, 300),
        health=100,
        strength=45,
        defense=8,
        speed=15,
        vitality=4,
        size=(32,32),
        x=400,
        y=300,
    )
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            # Get keys pressed
            keys = pygame.key.get_pressed()
            # Update player movement
            player1.move(keys)
            # Draw everything
            map(screen)         # Draw the tiled map    
            screen.fill((0, 0, 0))  # Clear the screen
            player1.draw(screen)    # Draw the player
            pygame.display.flip()   # Update the display
            if event.type == pygame.QUIT:
                running = False    
        clock.tick(60)  # Cap the frame rate
    pygame.quit()
def map(screen):
    WHITE = (255, 255, 255)
    # Tile settings
    tile_size = 32  # Size of each tile
    grid_width = screen_width // tile_size  # Number of columns
    grid_height = screen_height // tile_size  # Number of rows

    # Load the background image (replace with your own image path)
    background_image = pygame.image.load("wood1.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    # Create a list of tiles
    tiles = []
    for row in range(grid_height):
        for col in range(grid_width):
            tile_rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            tiles.append(tile_rect)
        screen.blit(background_image, (0, 0))

        # Draw the grid (tiles)
        for tile in tiles:
            pygame.draw.rect(screen, WHITE, tile, 1)  # Draw tile outlines
    for wall in walls:
        wall.draw(screen)
# Run the game
main()
