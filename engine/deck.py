from card import Card, suits, ranks
from random import shuffle


class Deck:

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_card(self, amount=1):
        return tuple(self.all_cards.pop() for _ in range(amount))

    def needs_reset(self, threshold=20):
        return len(self.all_cards) <= threshold

    def reset(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle_deck()
