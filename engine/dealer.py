from hand import Hand


class Dealer:

    def __init__(self):
        self.name = "Dealer"
        self.hand = Hand()

    def play_turn(self, deck):

        while self.hand.value < 17:
            self.hand.add_card(deck.deal_card())
            if self.hand.bust:
                return self.hand.value

        return self.hand.value
