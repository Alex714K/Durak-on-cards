from Durak import Durak
from Player import Player
import Game


if __name__ == '__main__':
    game = Durak(Player([], 1), Player([], 2))
    Game.init()