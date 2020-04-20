import pygame
import sys
import random
from ball import Ball
from paddle import Paddle


class Game:
    def __init__(self):
        self.s_size = self.screen_w, self.screen_h = 1280, 960
        self.screen = None
        self.title = 'Pong'
        self.bg_color = pygame.Color('black')
        self.white = (255, 255, 255)
        self.game_font = None
        self.ball = self.player = self.opponent = None

    def game_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player.speed += self.player.speed_inc
                elif event.key == pygame.K_UP:
                    self.player.speed -= self.player.speed_inc
                #  if event.key == pygame.K_s:
                #      self.opponent.speed += self.opponent.speed_inc
                #  elif event.key == pygame.K_w:
                #      self.opponent.speed -= self.opponent.speed_inc
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.player.stop()
                #  if event.key == pygame.K_w or event.key == pygame.K_s:
                #      self.opponent.stop()

    def score_up(self, who):
        if who == "player":
            self.player.score += 1
        elif who == "opponent":
            self.opponent.score += 1

        # Reset ball back to center then send it to random direction
        self.ball.x = int(self.screen_w / 2)
        self.ball.y = int(self.screen_h / 2)
        self.ball.ball_speed_x *= random.choice((1, -1))
        self.ball.ball_speed_y *= random.choice((1, -1))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()

        # Set screen
        self.screen = pygame.display.set_mode(self.s_size)
        pygame.display.set_caption(self.title)

        # Shapes
        self.ball = Ball(self.screen, self.screen_w / 2, self.screen_h / 2)
        self.player = Paddle(self.screen,
                             int(self.screen_w - 20),
                             int(self.screen_h / 2 - 70))
        self.opponent = Paddle(self.screen, 20, int(self.screen_h / 2 - 70))

        self.game_font = pygame.font.Font("freesansbold.ttf", 32)
        while True:
            # Handle input
            self.game_input()

            # Draw shapes
            self.screen.fill(self.bg_color)
            self.player.draw()
            self.opponent.draw()
            self.ball.draw()
            pygame.draw.aaline(self.screen,
                               self.white,
                               (self.screen_w / 2, 0),  # Start coordinate
                               (self.screen_w / 2, self.screen_h))  # End coordinate

            # Animations
            winner = self.ball.move(self.screen_w,
                                    self.screen_h,
                                    self.player,
                                    self.opponent)
            self.player.move(self.screen_h)
            self.opponent.move(self.screen_h)
            self.opponent.move_ai(self.ball)

            if winner is not None:
                self.score_up(winner)

            # Text
            player_text = self.game_font.render(f"{self.player.score}",
                                                True,
                                                self.white)
            opponent_text = self.game_font.render(f"{self.opponent.score}",
                                                  True,
                                                  self.white)
            self.screen.blit(player_text, (660, 470))
            self.screen.blit(opponent_text, (600, 470))

            #  pygame.display.update()
            pygame.display.flip()  # Outputs to display
            clock.tick(60)  # Game tick 60 FPS
