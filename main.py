from Durak import Durak
from Player import Player
from Game import Game
import pygame


if __name__ == '__main__':
    durak = Durak(Player([], 1), Player([], 2))
    game = Game()
    running = True
    while running:
        running = game.update()
    pygame.quit()
