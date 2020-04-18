import pygame
import sys
import random


def game_input():
    global player_speed, opponent_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += player_speed_inc
            elif event.key == pygame.K_UP:
                player_speed -= player_speed_inc
            #  if event.key == pygame.K_s:
            #      opponent_speed += opponent_speed_inc
            #  elif event.key == pygame.K_w:
            #      opponent_speed -= opponent_speed_inc
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0
            #  if event.key == pygame.K_w or event.key == pygame.K_s:
            #      opponent_speed = 0


def physics():
    global ball_speed_x, ball_speed_y, player_speed, opponent_speed

    # Ball bounces the other way around if hits edge of the screen
    if ball.top <= 0 or ball.bottom >= s_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score_up("player")
    if ball.right >= s_width:
        score_up("opponent")

        # Ball baounce if hits player or opponent
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # player and opponent can't go offscreen
    if player.top <= 0 or player.bottom >= s_height:
        player_speed = 0
    if opponent.top <= 0 or opponent.bottom >= s_height:
        opponent_speed = 0


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed_inc
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed_inc


def score_up(who):
    global player_score, opponent_score, ball_speed_x, ball_speed_y

    if who == "player":
        player_score += 1
    else:
        opponent_score += 1

    # Reset ball back to center then send it to random direction
    ball.center = (int(s_width / 2), int(s_height / 2))
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


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

ball_speed_x = ball_speed_y = 7 * random.choice((1, -1))
player_speed_inc = opponent_speed_inc = 8
player_speed = opponent_speed = 0
player_score = opponent_score = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)
while True:
    # Handle input
    game_input()

    # Draw shapes
    screen.fill(bg_color)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, white, opponent)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (s_width / 2, 0),
                       (s_width / 2, s_height))

    # Animations
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += player_speed
    opponent.y += opponent_speed

    physics()
    opponent_ai()

    # Text
    player_text = game_font.render(f"{player_score}", True, white)
    opponent_text = game_font.render(f"{opponent_score}", True, white)
    screen.blit(player_text, (660, 470))
    screen.blit(opponent_text, (600, 470))

    pygame.display.flip()  # Outputs to display
    clock.tick(60)  # Game tick 60 FPS
