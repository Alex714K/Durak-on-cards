import pygame.surface
from Button import Button


def print_text(screen: pygame.surface.Surface, message: str, position: tuple):
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, position)


def menu(screen: pygame.surface.Surface):
    global but
    but.draw(screen)
    exit_but.draw(screen)
    print_text(screen, "Exit", (exit_but.position[0] + exit_but.size[0]/2 - 33, exit_but.position[1] + exit_but.size[1]/2 - 17))

    if but.left_down():
        print_text(screen, "Loading", (300, 300))
    if exit_but.left_click():
        return False
    else:
        return True


pygame.font.init()
but = Button((300, 300), (300, 100), (0, 255, 0), (0, 0, 255), (255, 0, 0))
exit_but = Button((600, 600), (200, 100), (255, 255, 255), (0, 0, 0), (0, 0, 0))
font = pygame.font.Font(None, 50)


