import pygame
import sys

import settings
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.FOV = settings.FOV

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f"FPS {self.clock.get_fps() :.2f} FOV {((180 / math.pi) * self.FOV ) :.1f}")

    def draw(self):
        # self.screen.fill("black")
        self.object_renderer.draw()
        # FOR DEBUG DRAW
        # self.map.draw()
        # self.player.draw()

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
