from chips import Chips


class Player:

    def __init__(self, name, chips_amount=100):
        self.name = name
        # self.hand = Hand()
        self.chips = Chips(chips_amount)
