import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# Set screen
s_size = s_width, s_height = 1280, 960
screen = pygame.display.set_mode(s_size)
pygame.display.set_caption('Pong')

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()  # Outputs to display
    clock.tick(60)  # Game tick 60 FPS
