import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# Set screen
s_size = s_width, s_height = 1280, 960
screen = pygame.display.set_mode(s_size)
pygame.display.set_caption('Pong')

# Shapes
ball_wh = (30, 30)
ball = pygame.Rect(int(s_width / 2 - ball_wh[0] / 2),
                   int(s_height / 2 - ball_wh[1] / 2), ball_wh[0], ball_wh[1])
player = pygame.Rect(int(s_width - 20), int(s_height / 2 - 70), 10, 140)
opponent = pygame.Rect(20, int(s_height / 2 - 70), 10, 140)

# Colors
bg_color = pygame.Color('black')
white = (255, 255, 255)
red = pygame.Color('red')

ball_speed_x = ball_speed_y = 7
player_speed = opponent_speed = 0
player_speed_inc = opponent_speed_inc = 8

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += player_speed_inc
            elif event.key == pygame.K_UP:
                player_speed -= player_speed_inc
            if event.key == pygame.K_s:
                opponent_speed += player_speed_inc
            elif event.key == pygame.K_w:
                opponent_speed -= player_speed_inc
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                opponent_speed = 0

    # Draw shapes
    screen.fill(bg_color)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (s_width / 2, 0),
                       (s_width / 2, s_height))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    player.y += player_speed
    opponent.y += opponent_speed

    if ball.top <= 0 or ball.bottom >= s_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= s_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    if player.top <= 0 or player.bottom >= s_height:
        player_speed = 0
    if opponent.top <= 0 or opponent.bottom >= s_height:
        opponent_speed = 0

    pygame.display.flip()  # Outputs to display
    clock.tick(60)  # Game tick 60 FPS
