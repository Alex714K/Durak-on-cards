import pygame
from Durak import Durak
from Player import Player
from Button import Button
from Menu import menu


def init():
    pygame.init()

    durak = Durak(Player([], 1), Player([], 2))

    size = width, height = 1920, 1080
    flag = pygame.FULLSCREEN
    screen = pygame.display.set_mode(size, flag)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Durak')
    pygame.display.get_desktop_sizes()

    # Создаем второй холст
    screen2 = pygame.Surface(screen.get_size())
    running = True

    x = 100
    y = 100
    window = 'menu'
    keys = pygame.key.get_pressed()

    but = Button((100, 100), (50, 100), (250, 250, 250), (250, 0, 250), (250, 0, 0))

    # Запускаем окно
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # pygame.draw.rect(screen, (0, 0, 0), (0, 0, size[0], height))
        screen.fill((200, 200, 200))

        if keys[pygame.K_LEFT]:
            but.position = (but.position[0] - 3, but.position[1])
        if keys[pygame.K_RIGHT]:
            but.position = (but.position[0] + 3, but.position[1])

        but.draw(screen)
        if window == 'menu':
            running = menu(screen)

        if but.left_click():
            pass

        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
