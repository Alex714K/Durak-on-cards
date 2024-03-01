import pygame.font
import pygame.surface
from Button import Button
from Durak import Durak
from Card import Card


def print_text(display: pygame.surface.Surface, message: str, position: tuple, color=(255, 255, 255), centre=False, size=50):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, color)
    if centre:
        x = position[0] - text.get_width()/2
        y = position[1] - text.get_height()/2
        display.blit(text, (x, y))
    else:
        display.blit(text, position)


def draw_card(display: pygame.surface.Surface, position: tuple, dignity: str, suit: str, size=34):
    font = pygame.font.Font(None, 35)
    # suit_txt = font.render(suit, True, (0, 0, 0))
    num_txt = font.render(dignity, True, (0, 0, 0))
    # x = 120 = width
    # y = 180 = height
    pygame.draw.rect(display, (250, 250, 250), (position[0], position[1], 60 * 2, 90 * 2))
    pygame.draw.rect(display, (0, 0, 0), (position[0], position[1], 60 * 2, 90 * 2), 2)
    if suit in ('spades', 'clubs', 'black', 'red'):
        color = (0, 0, 0)
    else:
        color = (255, 0, 0)
    print_text(display, dignity, (position[0] + 3, position[1] + 1), (25, 25, 25), size=size)
    print_text(display, suit, (position[0] + 3, position[1] + num_txt.get_height() + 1), color, size=size)


def show_cards(display: pygame.surface.Surface, cards: list, player: int, durak: Durak, att=True):
    lst_cards = list()
    dist = len(cards) * 60 * 2
    first = 1920 / 2 - dist / 2
    match player:
        case 1:
            y = 1080 - 180
        # case 2:
        #     y = 0
        case _:
            y = 0
    for i in range(len(cards)):
        x1 = first + 120 * i
        y1 = y
        dignity = cards[i].dignity
        suit = cards[i].suit
        draw_card(display, (x1, y1), str(dignity), suit)
        lst_cards.append(Button((x1, y1), (60 * 2, 90 * 2), (256, 256, 256), (256, 256, 256),
                                (256, 256, 256)))
        lst_cards[0].draw(display)
        if lst_cards[0].left_click():
            if att:
                durak.make_attack(Card(dignity, suit))
            else:
                durak.make_defend(Card(dignity, suit))


pygame.font.init()
