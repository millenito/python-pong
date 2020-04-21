import pygame
import random


class Ball:
    def __init__(self, screen, x, y):
        self.w = 30
        self.h = 30
        self.x = x
        self.y = y
        self.ball_speed_x = 9 * random.choice((1, -1))
        self.ball_speed_y = 9 * random.choice((1, -1))
        self.color = (255, 255, 255)
        self.screen = screen
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.ellipse(self.screen,
                                        self.color,
                                        (int(self.x - self.w / 2),
                                         int(self.y - self.h / 2),
                                         self.w,
                                         self.h))

    def move(self, screen_w, screen_h, p1, p2):
        # Keep moving the ball
        self.x += self.ball_speed_x
        self.y += self.ball_speed_y

        # Ball bounces the other way around if hits edge of the screen
        if self.y <= 0 or self.y >= screen_h:
            self.ball_speed_y *= -1

        # Ball baounce if hits player or opponent
        if self.rect.colliderect(p1.rect):
            self.ball_speed_x *= -1
            self.x = p1.x - 15  # Move slightly besides paddle, clipping bug
        if self.rect.colliderect(p2.rect):
            self.ball_speed_x *= -1
            self.x = p2.x + 25  # Move slightly besides paddle, clipping bug

        if self.rect.left <= 0:
            return p1
        if self.rect.right >= screen_w:
            return p2

        return None
