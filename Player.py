from Card import Card


class Player:
    def __init__(self, cards: list, num: int):
        self.cards = cards
        self.num = num

    def return_card(self, dignity: (int, str), suit: str):
        return self.cards[self.cards.index(Card(dignity, suit))]
