from chips import Chips
from hand import Hand


class Player:

    def __init__(self, chips_amount=100):
        self.name = "Player"
        self.hand = Hand()
        self.chips = Chips(chips_amount)
