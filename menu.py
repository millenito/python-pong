import pygame
import sys


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None, font_color=(0, 0, 0)):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y -
                                            2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font("freesansbold.ttf", 32)
            text = font.render(self.text, 1, font_color)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                            self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


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
                          "Single Player")
        b_multi = Button(self.bg_color,
                         (self.screen_w / 2) - 120,
                         (self.screen_h / 2) - 20,
                         250,
                         100,
                         "Multi Player")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.render_text('Pong', self.white,
                             self.screen_w / 2,
                             (self.screen_h / 2) - 270,
                             center=True)
            b_single.draw(self.screen, self.white, self.white)
            b_multi.draw(self.screen, self.white, self.white)

            pygame.display.flip()  # Outputs to display
