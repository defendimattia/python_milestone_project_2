from card import Card, suits, ranks
from random import shuffle


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_card(self, amount=1):
        return tuple(self.all_cards.pop() for _ in range(amount))

    