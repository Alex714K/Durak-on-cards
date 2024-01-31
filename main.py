from Durak import Durak
from Player import Player
from Game import Game
import pygame


if __name__ == '__main__':
    game = Game()
    running = True
    while running:
        running = game.update()
    pygame.quit()
