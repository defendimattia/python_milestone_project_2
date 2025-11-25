class Chips:

    def __init__(self, total):
        self.total = total

    def bet(self, amount):
        self.total -= amount
        return amount

    def win(self, amount):
        self.total += amount * 2
        return amount * 2

    def can_bet(self, amount):
        return amount <= self.total
