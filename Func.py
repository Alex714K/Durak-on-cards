import pygame.font
import pygame.surface


def print_text(screen: pygame.surface.Surface, message: str, position: tuple, color=(255, 255, 255), centre=False, size=50):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, color)
    if centre:
        x = position[0] - text.get_width()/2
        y = position[1] - text.get_height()/2
        screen.blit(text, (x, y))
    else:
        screen.blit(text, position)


def draw_card(screen: pygame.surface.Surface, position: tuple, size_rect: tuple, num: str, suit: str, size=35):
    font = pygame.font.Font(None, 35)
    # suit_txt = font.render(suit, True, (0, 0, 0))
    num_txt = font.render(num, True, (0, 0, 0))
    pygame.draw.rect(screen, (250, 250, 250), (position[0], position[1], size_rect[0], size_rect[1]))
    if suit in ('spades', 'clubs', 'black', 'red'):
        color = (0, 0, 0)
    else:
        color = (255, 0, 0)
    print_text(screen, num, position, (25, 25, 25), size=size)
    print_text(screen, suit, (position[0], position[1] + num_txt.get_height()), color, size=size)


pygame.font.init()
