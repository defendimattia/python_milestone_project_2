from engine.dealer import Dealer
from engine.deck import Deck
from engine.player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

