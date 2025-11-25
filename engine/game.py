import os
from engine.dealer import Dealer
from engine.deck import Deck
from engine.player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.current_bet = None

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

    def start_game(self):
        self.player.hand.add_card(self.deck.deal_card(2))
        self.dealer.hand.add_card(self.deck.deal_card(2))

    def place_bet(self):
        print(f"Your current balance is: ${self.player.chips.total}")

        while True:
            current_bet = input("Place your bet: ")

            try:
                current_bet = int(current_bet)

                if current_bet <= 0:
                    print("You cannot bet 0. Retry.\n")
                    continue

                if not self.player.chips.can_bet(current_bet):
                    print("Your bet exceeds your total balance. Retry.\n")
                    continue

                self.player.chips.bet(current_bet)
                self.current_bet = current_bet
                print(f"Your bet is: ${current_bet}\n")
                break

            except ValueError:
                print("This is not a valid number. Retry.\n")
