import pygame

if __name__ == "__main__":
    from menu import Menu
    pygame.init()

    screen_w, screen_h = 1280, 960
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption('Pong')

    game = Menu(screen)
    game.draw()
