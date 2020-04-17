import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# Set screen
s_size = s_width, s_height = 1280, 960
screen = pygame.display.set_mode(s_size)
pygame.display.set_caption('Pong')

# Shapes
ball_w = 30
ball_h = 30
ball = pygame.Rect(int(s_width / 2 - ball_w / 2),
                   int(s_height / 2 - ball_h / 2), ball_w, ball_h)
player = pygame.Rect(int(s_width - 20), int(s_height / 2 - 70), 10, 140)
opponent = pygame.Rect(20, int(s_height / 2 - 70), 10, 140)

# Colors
bg_color = pygame.Color('black')
white = (255, 255, 255)
red = pygame.Color('red')

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw shapes
    screen.fill(bg_color)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (s_width / 2, 0),
                       (s_width / 2, s_height))

    pygame.display.flip()  # Outputs to display
    clock.tick(60)  # Game tick 60 FPS
