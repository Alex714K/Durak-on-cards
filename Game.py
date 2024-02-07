import pygame
# import numpy
from Durak import Durak
from Player import Player
from Button import Button
from Func import *


class Game:
    def __init__(self):
        pygame.init()

        first_player = Player([], 1)
        second_player = Player([], 2)
        self.durak = Durak(first_player, second_player)

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
        self.check_end = 0
        self.ai = None

        self.window = 'menu'
        self.keys = pygame.key.get_pressed()

        self.colors = {"exit": (87, 255, 106),
                       "exit_aim": (60, 240, 80),
                       "exit_down": (50, 220, 70),
                       "play": (50, 255, 50),
                       "play_aim": (35, 240, 35),
                       "play_down": (20, 225, 20),
                       "options": (0, 0, 0),
                       "options_aim": (25, 25, 25),
                       "options_down": (50, 50, 50),
                       "card": (250, 250, 250),
                       "reset": (0, 0, 0),
                       "board": (84, 32, 13)}

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     but.position = (but.position[0] - 3, but.position[1])
        # if keys[pygame.K_RIGHT]:
        #     but.position = (but.position[0] + 3, but.position[1])
        # if pygame.mouse.get_pressed()[0]:
        #     print(pygame.mouse.get_pos())
        # but.draw(screen)
        #  Вызывает меню/основную игру/настройки
        if self.window == 'game':
            self.running = self.game()
        elif self.window == 'menu':
            self.running = self.menu()
        elif self.window == 'options':
            self.running = self.options()
        elif self.window == 'who':
            self.running = self.vs_who()
        elif self.window == 'loading':
            self.running = self.loading()
        self.clock.tick(100)
        # проверка на выключение игры
        if self.running:
            return True
        else:
            return False

    def menu(self):
        self.display.fill((255, 255, 255))
        if len(self.buttons) < 1:
            # 0 play button
            self.buttons.append(Button((1920/2 - 100, 1080/2 - 50 - 100), (200, 100), self.colors["play"],
                                       self.colors["play_aim"], self.colors["play_down"], "Play"))
            # 1 options button
            self.buttons.append(Button((1920/2 - 100, 1080/2 - 50 + 100), (200, 100), self.colors["options"],
                                       self.colors["options_aim"], self.colors["options_down"], "Options"))
            # 2 exit button
            self.buttons.append(Button((1920 - 200, 1080 - 100), (200, 100), self.colors["exit"],
                                       self.colors["exit_aim"], self.colors["exit_down"], "Exit"))
        self.buttons[0].draw(self.display)

        if self.buttons[0].left_down():
            print_text(self.display, "Loading", (300, 300))
            self.window = 'who'
            self.buttons.clear()
            return True
        if self.buttons[1].draw_left_click(self.display):
            self.window = 'options'
            self.buttons.clear()
            return True
        if self.buttons[2].draw_left_click(self.display):
            return False

        pygame.display.flip()
        return True

    def options(self):
        self.display.fill((255, 255, 255))
        if len(self.buttons) < 1:
            # 0 exit button
            self.buttons.append(Button((1920 - 200, 1080 - 100), (200, 100), self.colors["exit"],
                                       self.colors["exit_aim"], self.colors["exit_down"], "Exit"))
            # 1 reset
            self.buttons.append(Button((1920/2 - 100, 1080/2 - 50), (200, 100), self.colors["reset"],
                                       (40, 40, 40), (75, 75, 75), "Reset?"))

        if self.buttons[0].draw_left_click(self.display):
            self.window = 'menu'
            self.buttons.clear()
            return True
        if self.buttons[1].draw_left_click(self.display):
            self.buttons[1].text = "I can't)"

        pygame.display.flip()
        return True

    def game(self):
        self.display.fill((235, 235, 235))
        if len(self.buttons) < 1:
            # 0 exit button
            self.buttons.append(Button((1920 - 200, 1080 - 100), (200, 100), self.colors["exit"],
                                       self.colors["exit_aim"], self.colors["exit_down"], "Exit"))
        draw_card(self.display, (400, 400), (60*2, 90*2), 'A', 'diamonds')

        # столы игроков (ага, конечно, два коричневых прямоугольника, очень похожи на столы =) )
        pygame.draw.rect(self.display, self.colors["board"], (1920/2 - 300, 1080 - 200, 600, 200))
        pygame.draw.rect(self.display, self.colors["board"], (1920/2 - 300, 0, 600, 200))
        # где какой игрок (строгое расположение)
        print_text(self.display, "1", (1920 / 2 - 300 - 25, 1080 - 30), (0, 0, 0))
        print_text(self.display, "2", (1920 / 2 - 300 - 25, 0), (0, 0, 0))

        if self.buttons[0].draw_left_click(self.display):
            return False
        if self.check_end == 5:
            if self.durak.end_or_not():
                return False
            else:
                self.check_end = 0
        else:
            self.check_end += 1

        pygame.display.flip()
        return True

    def vs_who(self):
        self.display.fill((255, 255, 255))
        if len(self.buttons) < 1:
            # 0 vs player
            self.buttons.append(Button((1920/2 - 200 - 100, 1080/2 - 50), (200, 100), (256, 256 ,256),
                                       (250, 250, 250), (256, 256, 256), "VS Player", (0, 0, 0)))
            # 1 vs AI
            self.buttons.append(Button((1920/2 + 200 - 100, 1080/2 - 50), (200, 100), (256, 256, 256),
                                       (250, 250, 250), (256, 256, 256), "VS AI", (0, 0, 0)))
        self.buttons[1].draw(self.display)
        print_text(self.display, str(len(self.buttons)), (50, 50), (0, 0, 0))
        if self.buttons[0].draw_left_click(self.display):
            self.ai = False
            self.window = 'loading'
            self.buttons.clear()
        if self.buttons[1].left_click():
            self.ai = True
            self.window = 'loading'
            self.buttons.clear()
        pygame.display.flip()
        return True

    def loading(self):
        self.display.fill((0, 0, 0))
        print_text(self.display, "Loading)", (1920/2, 1080/2), centre=True)
        pygame.display.flip()
        pygame.time.delay(500)
        self.window = 'game'
        return True

