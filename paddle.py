import pygame


class Paddle:
    def __init__(self, screen, x, y):
        self.w = 10
        self.h = 140
        self.x = x
        self.y = y
        self.speed = 0
        self.speed_inc = 8
        self.score = 0
        self.color = (255, 255, 255)
        self.screen = screen
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x,
                                                               self.y,
                                                               self.w,
                                                               self.h))

    def move(self, screen_h):
        self.y += self.speed

        # Can't go offscreen
        if self.rect.top <= 0:
            self.stop()
        if self.rect.bottom >= screen_h:
            self.stop()

    def stop(self):
        self.speed = 0

    def move_ai(self, ball):
        if self.rect.bottom < ball.y:
            self.y += self.speed_inc
        if self.rect.top > ball.y:
            self.y -= self.speed_inc
