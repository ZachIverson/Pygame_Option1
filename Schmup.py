# --------------------------------------------
# Zach Ignacio - Shmup Game Starter
# Date: April 27, 2025
# Description: Basic player movement in Pygame
# --------------------------------------------

import pygame
import random

# Game window dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
FPS = 60

# Color definitions (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize Pygame and create a window
pygame.init()
pygame.mixer.init()  # for future sound effects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Schmup! (Zach Ignacio Version)")
clock = pygame.time.Clock()

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speed_x = -8
        if keys[pygame.K_d]:
            self.speed_x = 8
        self.rect.x += self.speed_x

        # Keep player inside the screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Group to hold all sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
