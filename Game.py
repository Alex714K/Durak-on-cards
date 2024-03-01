import pygame
from Player import Player
from Func import *


class Game:
    def __init__(self):
        pygame.init()

        self.attacker = Player([], 1)
        self.defender = Player([], 2)
        self.durak = Durak(self.attacker, self.defender)

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
                       "play": (87, 255, 106),
                       "play_aim": (60, 240, 80),
                       "play_down": (50, 220, 70),
                       "options": (0, 0, 0),
                       "options_aim": (25, 25, 25),
                       "options_down": (50, 50, 50),
                       "card": (250, 250, 250),
                       "reset": (0, 0, 0),
                       "board": (50, 200, 40),
                       "gold": (240, 235, 0)}

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        #  Вызывает меню/основную игру/настройки
        match self.window:
            case 'game':
                self.running = self.game()
            case 'menu':
                self.running = self.menu()
            case 'options':
                self.running = self.options()
            case 'who':
                self.running = self.vs_who()
            case 'loading':
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
        # где какой игрок
        match self.durak.who_attack():
            case 1:
                print_text(self.display, "Attacker", (0, 1080 - 30), (0, 0, 0))
                print_text(self.display, "Defender", (0, 0), (0, 0, 0))
                show_cards(self.display, self.attacker.cards, 1, self.durak)

            case 2:
                print_text(self.display, "Defender", (0, 1080 - 30), (0, 0, 0))
                print_text(self.display, "Attacker", (0, 0), (0, 0, 0))
                show_cards(self.display, self.attacker.cards, 2, self.durak)

        if self.buttons[0].draw_left_click(self.display):
            self.buttons.clear()
            self.window = 'menu'
            return True
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
        if len(self.buttons) < 2:
            # 0 vs player
            self.buttons.append(Button((1920/2 - 200 - 100, 1080/2 - 50), (200, 100), (256, 256 ,256),
                                       (250, 250, 250), (256, 256, 256), "VS Player", (0, 0, 0)))
            # 1 vs AI
            self.buttons.append(Button((1920/2 + 200 - 100, 1080/2 - 50), (200, 100), (256, 256, 256),
                                       (250, 250, 250), (256, 256, 256), "VS AI", (0, 0, 0)))
        self.buttons[1].draw(self.display)
        if self.buttons[0].draw_left_click(self.display):
            self.ai = False
            self.window = 'loading'
            self.buttons.clear()
            return True
        if self.buttons[1].left_click():
            self.ai = True
            self.window = 'loading'
            self.buttons.clear()
            return True
        pygame.display.flip()
        return True

    def loading(self):
        self.display.fill((0, 0, 0))
        print_text(self.display, "Loading)", (1920/2, 1080/2), centre=True)
        pygame.display.flip()
        pygame.time.delay(500)
        self.window = 'game'
        return True
