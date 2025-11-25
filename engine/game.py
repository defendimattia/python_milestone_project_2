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

    def deal_initial_cards(self):
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

    def display_hands(self, initial_hand=False):

        player_cards = ", ".join(str(card) for card in self.player.hand.cards)
        print(f"Player hand: {player_cards} (Value: {self.player.hand.value})")

        if initial_hand:

            if self.dealer.hand.cards:
                print(f"Dealer hand: {self.dealer.hand.cards[0]}, [Hidden Card]")

        else:
            dealer_cards = ", ".join(str(card) for card in self.dealer.hand.cards)
            print(f"Dealer hand: {dealer_cards} (Value: {self.dealer.hand.value})")

    def hit_or_stand(self):

        while True:

            player_input = input("Hit or Stand? (h/s)")

            if player_input.lower() not in ("h", "s"):
                print("Answer not valid. Retry\n")
            else:
                return player_input

    def player_turn(self):
        print("Player's turn...")

        while True:
            self.clear_screen()
            self.display_hands(True)
            hit_or_stand = self.hit_or_stand()

            if hit_or_stand == "h":
                self.player.hand.add_card(self.deck.deal_card())
                if self.player.hand.bust:
                    break

            if hit_or_stand == "s":
                break

    def dealer_turn(self):
        print("Dealer's turn...")

        dealer_value = self.dealer.play_turn(self.deck)

        self.display_hands()

        return dealer_value

    def resolve_round(self):

        if self.player.hand.has_blackjack():
            print("B L A C K J A C K !")
            print("Player WINS!")
            self.player.chips.win(self.current_bet)
            return f"Player won ${self.current_bet * 2}"

        if self.dealer.hand.has_blackjack():
            print("B L A C K J A C K !")
            print("Dealer WINS!")
            return None

        if self.player.hand.bust:
            print("Player busts! Dealer wins!")
            return "Dealer WINS!"

        if self.dealer.hand.bust:
            print("Dealer busts! Player wins!")
            self.player.chips.win(self.current_bet)
            return f"Player won ${self.current_bet * 2}"

        if self.player.hand.value > self.dealer.hand.value:
            self.player.chips.win(self.current_bet)
            print("Player WINS!")
            return f"Player won ${self.current_bet * 2}"

        if self.dealer.hand.value > self.player.hand.value:
            print("Dealer WINS!")
            return "Dealer WINS!"

        if self.player.hand.value == self.dealer.hand.value:
            print("Tie! No one won!")

    def reset_round(self):
        self.player.hand.reset()
        self.dealer.hand.reset()
        self.current_bet = None
        if self.deck.needs_reset():
            self.deck.reset()

    def play_round(self):
        self.reset_round()

        self.place_bet()

        self.deal_initial_cards()

        self.display_hands(initial_hand=True)

        self.player_turn()

        if not self.player.hand.bust:
            self.dealer_turn()

        result = self.resolve_round()
        print(result)

    def play_game(self):
        self.show_welcome_message()

        while True:
            self.play_round()

            while True:
                keep_going = input("Wanna play another round? (y/n): ")

                if keep_going.lower() == "y":
                    self.clear_screen()
                    break

                elif keep_going.lower() == "n":
                    return "Thank you for playing!"

                else:
                    print("Answer not valid. Retry.\n")
