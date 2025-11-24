class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.bust = False

    def reset(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.bust = False

    def add_card(self, cards):
        self.cards.extend(cards)

        for card in cards:
            self.value += card.value

            if card.rank == "Ace":
                self.aces += 1

        self.check_status()

    def adjust_for_aces(self):

        count = self.aces

        while self.value > 21 and count > 0:
            self.value -= 10
            count -= 1

    def check_status(self):

        if self.value > 21 and self.aces > 0:
            self.adjust_for_aces()
        elif self.value > 21 and self.aces == 0:
            self.bust = True

    def has_blackjack(self):
        return self.value == 21 and len(self.cards) == 2
