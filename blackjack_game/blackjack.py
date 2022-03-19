from asci_art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suit = ["Hearts", ]


def deal_card():
    """:returns a random card from the deck"""
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("Blackjack")
        return 0

    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, dealer_score):
    if user_score > 21:
        return  "You lose, went over 21"
    elif dealer_score > 21:
        return  "Dealer lose, went over 21"
    elif dealer_score == user_score:
        return ("DRAW!")
    elif dealer_score > user_score:
        return ("Dealer Wins!")
    else:
        return "Player Wins!"


def play_game():

    print(logo)
    user_cards = []
    dealer_cards = []


    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())


    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)


    game_over = False
    while not game_over:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Dealer cards {[dealer_cards[0]]}, dealer score {dealer_score}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True

        else:
            choice = input("Would you like to hit or stay? h or s? ").casefold()
            while True:
                if choice == "h":
                    user_cards.append(deal_card())
                    break
                elif choice == "s":
                    game_over = True
                    break
                else:
                    choice = input("Please enter h to hit or s to stay: ")

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print(dealer_cards)

    print(f"Your cards {user_cards}, player final score {user_score}")
    print(f"Dealer cards {dealer_cards}, dealer final score {dealer_score}")
    print(compare(user_score, dealer_score))


p = input("Do you want to play another game y/n? ").casefold()

if p == "y":
    play_game()
else:
    quit()

