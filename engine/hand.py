class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def reset(self):
        self.cards = []
        self.value = 0
        self.aces = 0
