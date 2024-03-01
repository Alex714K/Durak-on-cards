from random import choice, sample, shuffle
from Player import Player
from Card import Card


class Durak:
    def __init__(self, player1: Player, player2, ai_flag=False):
        self.board = list()
        [self.attacker, self.defender] = sample([player1, player2], k=2)
        self.ai_flag = ai_flag
        self.winner = None
        self.dignitys_str = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.dignitys = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        # diamonds hearts spades clubs  бубны черви пики крести
        self.suits = ['diamonds', 'hearts', 'spades', 'clubs']
        self.trump = choice(self.suits)
        self.standard_deck = list()
        self.make_deck()
        self.standard_deck.append(Card('Joker', 'black'))
        self.standard_deck.append(Card('Joker', 'red'))

        deck1 = sample(self.standard_deck, k=6)
        self.give_cards(deck1, self.attacker)
        deck2 = sample(self.standard_deck, k=6)
        self.give_cards(deck2, self.defender)

    def end_or_not(self):
        end = False
        if len(self.standard_deck) == 0:  # Проверка окончания игры
            if len(self.defender.cards) == 0:
                end = True
                self.winner = self.defender.num
            elif len(self.attacker.cards) == 0:
                end = True
                self.winner = self.attacker.num
        return end

    def make_attack(self, cards: (list, int)):
        if type(cards) is not list:
            cards = [cards]
        for card in cards:
            self.board.append([card, ])
            self.attacker.cards.pop(card)
        print('make_attack complete!')

    def make_defend(self, cards: (list, int)):
        if type(cards) is not list:
            cards = [cards]
        # end = False
        need_to_delete = list()
        if len(self.board) == 0:
            for i, card in enumerate(cards):
                from_board = self.board[i]
                if card.suit == self.trump and from_board.suit != self.trump:
                    print(f"Карта {card.suit} {card.dignity} закрыта.")
                    need_to_delete.append([from_board, card])
                elif card.suit == from_board.suit:
                    if card.dignity > from_board.dignity:
                        print(f"Карта {card.suit} {card.dignity} закрыта.")
                        need_to_delete.append([from_board, card])
                else:
                    print(f"You can't def {from_board.suit} {from_board.dignity} with this {card.suit} {card.dignity}")
        else:
            print("nothing to def")
        print('make_defend complete!')
        self.close_cards(need_to_delete)

    def give_cards(self, cards: (list, int), player: Player):
        if type(cards) is not list:
            cards = [cards]
        for card in cards:
            player.cards.append(card)
            self.standard_deck.remove(card)

    @staticmethod
    def take_cards(cards: (list, int), player: Player):
        if type(cards) is not list:
            cards = [cards]
        for card in cards:
            player.cards.remove(card)

    def close_cards(self, deck: list):
        # if type(deck) is not list:
        #     deck = [deck]
        for cards in deck:
            ind = self.board.index(cards[1])
            self.board[ind] = cards
        pass

    def who_attack(self):
        return self.attacker.num

    def who_defend(self):
        return self.defender.num

    def make_deck(self):
        for dign in self.dignitys:
            for suit in self.suits:
                self.standard_deck.append(Card(str(dign), suit))
        shuffle(self.standard_deck)
        print(self.standard_deck[0].dignity)

    def end_turn(self):
        self.board.clear()
