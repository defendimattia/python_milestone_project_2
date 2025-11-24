from hand import Hand


class Dealer:

    def __init__(self):
        self.name = "Dealer"
        self.hand = Hand()

    def play_turn(self, deck):

        if self.hand.has_blackjack():
            return True

        while self.hand.value < 17:
            self.hand.add_card(deck.deal_card())
