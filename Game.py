import pygame
# import numpy
from Durak import Durak
from Player import Player
from Button import Button
from Func import *


class Game:
    def __init__(self):
        pygame.init()

        self.durak = Durak(Player([], 1), Player([], 2))

        self.size = 1920, 1080
        flag = pygame.SCALED  # черные полосы при другом разрешении
        self.display = pygame.display.set_mode(self.size, flag)
        flag = pygame.FULLSCREEN  # полный экран
        self.display = pygame.display.set_mode(self.size, flag)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Durak')

        # Список с кнопками
        self.buttons = list()

        self.running = True

        self.window = 'menu'
        self.keys = pygame.key.get_pressed()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        self.display.fill((255, 255, 255))
        # if keys[pygame.K_LEFT]:
        #     but.position = (but.position[0] - 3, but.position[1])
        # if keys[pygame.K_RIGHT]:
        #     but.position = (but.position[0] + 3, but.position[1])
        # if pygame.mouse.get_pressed()[0]:
        #     print(pygame.mouse.get_pos())
        # but.draw(screen)
        #  Вызывает меню/основную игру/настройки
        if self.window == 'menu':
            self.running = self.menu()
        elif self.window == 'options':
            self.running = self.options()
        elif self.window == 'game':
            self.running = self.game()
        self.clock.tick(100)
        # проверка на выключение игры
        if self.running:
            return True
        else:
            return False

    def menu(self):
        if len(self.buttons) < 1:
            # 0 play button
            self.buttons.append(Button((1920/2 - 100, 1080/2 - 50 - 100), (200, 100), (0, 255, 0),
                                       (0, 0, 255), (255, 0, 0)))
            # 1 options button
            self.buttons.append(Button((1920/2 - 100, 1080/2 - 50 + 100), (200, 100), (0, 0, 0),
                                       (1, 1, 1), (256, 256, 256), "Options", (255, 255, 255)))
            # 2 exit button
            self.buttons.append(Button((1920 - 200, 1080 - 100), (200, 100), (87, 255, 106),
                                       (60, 240, 80), (50, 220, 70), "Exit"))
        self.buttons[0].draw(self.display)

        if self.buttons[0].left_down():
            print_text(self.display, "Loading", (300, 300))
        if self.buttons[1].draw_left_click(self.display):
            self.window = 'options'
            self.buttons.clear()
            return True
        if self.buttons[2].draw_left_click(self.display):
            return False

        pygame.display.flip()
        return True

    def options(self):
        if len(self.buttons) < 1:
            # 0 exit button
            self.buttons.append(Button((1920 - 200, 1080 - 100), (200, 100), (87, 255, 106),
                                       (87, 255, 106), (87, 255, 106), text="Exit"))

        if self.buttons[0].draw_left_click(self.display):
            return False

        pygame.display.flip()
        return True

    def game(self):
        return False
