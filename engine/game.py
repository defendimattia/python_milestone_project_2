import os
from engine.dealer import Dealer
from engine.deck import Deck
from engine.player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def show_welcome_message(self):
        self.clear_screen()
        print("🎲 Welcome to Blackjack! 🎲")
        print("Quick rules:")
        print("- Goal: reach 21 without going bust")
        print("- Face cards (J, Q, K) are worth 10, Ace is 1 or 11")
        print("- Dealer hits until reaching at least 17")
        print("- You can choose your bet each round")
        print("Good luck!\n")
