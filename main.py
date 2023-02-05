import pygame
import sys
from settings import *
from map import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f"{self.clock.get_fps() :.2f}")

    def draw(self):
        self.screen.fill("black")
        self.map.draw()

    def run(self):
        while True:
            self.checking_events()
            self.update()
            self.draw()

    @staticmethod
    def checking_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
