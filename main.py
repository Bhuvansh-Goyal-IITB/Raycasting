import pygame
from settings import *
from game_states import GameStates
from game_window import RayCastingGame
from sys import exit
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.state = GameStates.game

        self.game = RayCastingGame(self)

    def loop(self):
        while True:
            if self.state == GameStates.quit:
                pygame.quit()
                exit()
            elif self.state == GameStates.game:
                self.game.loop()

    def set_state(self, state):
        self.state = state

if __name__ == "__main__":
    game = Game()
    game.loop()