import pygame

if __name__ == "__main__":
    from game import Game
    pygame.init()

    screen_w, screen_h = 1280, 960
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption('Pong')

    game = Game(screen)
    game.run()
