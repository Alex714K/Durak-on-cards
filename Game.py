from random import choice, sample


class Card:
    def __init__(self, dignity: str, suit: str):
        self.dignity = dignity
        self.suit = suit


class Player:
    def __init__(self, cards: list, num: int):
        self.cards = cards
        self.num = num

    def return_card(self, dignity: str, suit: str):
        return self.cards[self.cards.index(Card(dignity, suit))]


class Durak:
    def __init__(self, player1: Player, player2, ai_flag=False):
        self.board = list()
        self.player1 = player1
        self.player2 = player2
        [self.attacker, self.defender] = sample([self.player1, self.player2], k=2)
        self.ai_flag = ai_flag
        self.winner = None
        self.dignitys = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # diamonds hearts spades clubs  бубны черви пики крести
        self.suits = ['diamonds', 'hearts', 'spades', 'clubs']
        self.trump = choice(self.suits)
        self.standard_deck = list()
        for dign in self.dignitys:
            for suit in self.suits:
                self.standard_deck.append(Card(dign, suit))
        self.standard_deck.append(Card('Joker', 'Black'))
        self.standard_deck.append(Card('Joker', 'Red'))

        deck1 = sample(self.standard_deck, k=6)
        self.give_cards(deck1, self.player1)
        self.remove_deck(deck1)
        deck2 = sample(self.standard_deck, k=6)
        self.give_cards(deck2, self.player2)
        self.remove_deck(deck2)

        # self.init_game()

    def init_game(self):
        end = False
        if len(self.standard_deck) == 0:  # Проверка окончания игры
            if len(self.defender.cards) == 0:
                end = True
                self.winner = self.defender.num
            elif len(self.attacker.cards) == 0:
                end = True
                self.winner = self.attacker.num

            self.attacker, self.defender = self.defender, self.attacker

    def make_attack(self, *cards):
        for card in cards:
            self.board.append([card, ])

    def make_defend(self, *cards):
        if len(self.board) == 0:
            need_to_delete = list()
            for i, card in enumerate(cards):
                from_board = self.board[i]
                if card.suit == self.trump and from_board.suit != self.trump:
                    need_to_delete.append(from_board)
                elif card.suit == from_board.suit:
                    if self.dignitys.index(card.dignity) > self.dignitys.index(from_board.dignity):
                        need_to_delete.append(card)
                else:
                    print('Не подходит')

    def give_cards(self, cards: (list, str), player: Player):
        if type(cards) is not list:
            cards = [cards]
        for card in cards:
            player.cards.append(card)

    def remove_deck(self, deck: list):
        for card in deck:
            self.standard_deck.remove(card)

    def who_attack(self):
        return self.attacker.num

    def who_defend(self):
        return self.defender.num


Durak(Player([], 1), Player([], 2))
