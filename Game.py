import pygame
# import numpy
from Durak import Durak
from Player import Player
from Button import Button
from Func import *


pygame.font.init()


class Game:
    def __init__(self):
        pygame.init()

        self.durak = Durak(Player([], 1), Player([], 2))

        self.size = width, height = 2880, 1800
        flag = pygame.FULLSCREEN
        self.display = pygame.display.set_mode(self.size, flag)
        self.size = self.display.get_size()
        self.display = pygame.display.set_mode(self.size, flag)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Durak')
        pygame.display.get_desktop_sizes()

        # Кнопки
        self.buttons = list()

        # self.screen2 = pygame.Surface(self.screen.get_size())
        self.running = True

        # x = 100
        # y = 100
        self.window = 'menu'
        self.keys = pygame.key.get_pressed()

        # but = Button((100, 100), (50, 100), (250, 250, 250), (250, 0, 250), (250, 0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        self.display.fill((200, 200, 200))
        # if keys[pygame.K_LEFT]:
        #     but.position = (but.position[0] - 3, but.position[1])
        # if keys[pygame.K_RIGHT]:
        #     but.position = (but.position[0] + 3, but.position[1])
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())
        # but.draw(screen)
        #  Вызывает меню, основную игру, настройки
        if self.window == 'menu':
            self.running = self.menu()
        elif self.window == 'options':
            pass
        elif self.window == 'game':
            pass
        self.clock.tick(100)
        if self.running:
            return True
        else:
            return False

    def menu(self):
        if len(self.buttons) < 1:
            # 0 but
            self.buttons.append(Button((300, 300), (300, 100), (0, 255, 0), (0, 0, 255), (255, 0, 0)))
            # 1 exit button
            self.buttons.append(Button((1000 - 200, 1000 - 100), (200, 100), (255, 255, 255), (0, 0, 0), (0, 0, 0), text="Exit"))

        self.buttons[0].draw(self.display)
        self.buttons[1].draw(self.display)

        if self.buttons[0].left_down():
            print_text(self.display, "Loading", (300, 300))
        pygame.display.flip()
        if self.buttons[1].left_click():
            return False
        return True

