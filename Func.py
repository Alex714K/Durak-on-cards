import pygame.surface


def print_text(screen: pygame.surface.Surface, message: str, position: tuple):
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, position)


pygame.font.init()
font = pygame.font.Font(None, 50)