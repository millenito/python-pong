import pygame
import sys
from game import Game
from button import Button


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_w, self.screen_h = pygame.display.get_surface().get_size()
        self.bg_color = pygame.Color('black')
        self.white = (255, 255, 255)

    def render_text(self, text, color, x, y, center=False):
        game_font = pygame.font.Font("freesansbold.ttf", 102)
        rendered = game_font.render(text, True, color)
        if center:
            rendered_rect = rendered.get_rect(center=(x, y))
            self.screen.blit(rendered, rendered_rect)
        else:
            self.screen.blit(rendered, (x, y))

    def draw(self):
        b_single = Button(self.bg_color,
                          (self.screen_w / 2) - 120,
                          (self.screen_h / 2) - 50,
                          250,
                          100,
                          "Single Player",
                          self.white)
        b_multi = Button(self.bg_color,
                         (self.screen_w / 2) - 120,
                         (self.screen_h / 2) + 90,
                         250,
                         100,
                         "Multi Player",
                         self.white)
        while True:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b_single.isOver(mouse_pos):
                        game = Game(self.screen, 'single')
                        game.run()
                    elif b_multi.isOver(mouse_pos):
                        game = Game(self.screen, 'double')
                        game.run()

                if event.type == pygame.MOUSEMOTION:
                    if b_single.isOver(mouse_pos):
                        b_single.color = self.white
                        b_single.text_color = self.bg_color
                    else:
                        b_single.color = self.bg_color
                        b_single.text_color = self.white

                    if b_multi.isOver(mouse_pos):
                        b_multi.color = self.white
                        b_multi.text_color = self.bg_color
                    else:
                        b_multi.color = self.bg_color
                        b_multi.text_color = self.white

            self.screen.fill(self.bg_color)
            self.render_text('Pong', self.white,
                             self.screen_w / 2,
                             (self.screen_h / 2) - 270,
                             center=True)
            b_single.draw(self.screen, self.white)
            b_multi.draw(self.screen, self.white)

            pygame.display.flip()  # Outputs to display
