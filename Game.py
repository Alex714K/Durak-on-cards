from random import choice, sample


class Card:
    def __init__(self, dignity: str, suit: str):
        self.dignity = dignity
        self.suit = suit


class Player:
    def __init__(self, cards: list):
        self.cards = cards

    def return_card(self, dignity: str, suit: str):
        return self.cards[self.cards.index(Card(dignity, suit))]


class Durak:
    def __init__(self, player1: Player, player2, ai_flag=False):
        self.player1 = player1
        self.player2 = player2
        self.ai_flag = ai_flag
        dignity = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A', '']
        # diamonds hearts spades clubs  бубны черви пики крести
        suits = ['diamonds', 'hearts', 'spades', 'clubs']
        trump = choice(suits)  # заменить на рандом
        self.standard_deck = list()
        for dign in dignity:
            for suit in suits:
                self.standard_deck.append(Card(dign, suit))

        deck1 = sample(self.standard_deck, k=6)
        self.give_cards(deck1, self.player1)
        self.remove_deck(deck1)
        deck2 = sample(self.standard_deck, k=6)
        self.give_cards(deck2, self.player2)
        self.remove_deck(deck2)

        self.init_game()

    def init_game(self):
        player1 = self.player1
        player2 = self.player2
        end = True
        while True:
            if end:
                break
            pass

    def give_cards(self, cards: (list, str), player: Player):
        if type(cards) != type(list()):
            cards = [cards]
        for card in cards:
            player.cards.append(card)

    def remove_deck(self, deck: list):
        for card in deck:
            self.standard_deck.remove(card)

    def players_turn(self):
        return None


# diamonds hearts spades clubs  бубны черви пики крести
Durak(Player([]), Player([]))
