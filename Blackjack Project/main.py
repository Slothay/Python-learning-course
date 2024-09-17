import random

import art


def end_of_game(p_cards, p_score, c_cards, c_score):
    """Print the final results of the game."""
    print(f"Your cards: {p_cards}, final score: {p_score}")
    print(f"Computer's final hand: {c_cards}, final score: {c_score}")
    if p_score > 21:
        print("Bust! You lose.")
    elif c_score > 21:
        print("You win!")
    elif p_score == 0:
        print("Blackjack! You win!")
    elif c_score == 0:
        print("You lose. Your opponent had Blackjack.")
    elif p_score < c_score < 21:
        print("Bust! You lose.")
    elif c_score < p_score < 21:
        print("You win!")
    else:
        print("It's a draw!")

def new_card_player(player_cards):
    """Add new card to the deck and check if Ace is 11 or 1."""
    new_card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if new_card_choice == 'y':
        new_card_to_add = random.choice(cards)
        if (new_card_to_add == 11) and (11 + sum(player_cards) > 21):
            new_card_to_add = 1
        player_cards.append(new_card_to_add)
        return True
    else:
        return False

def new_card_computer(computer_cards):
    new_computer_card = random.choice(cards)
    if (new_computer_card == 11) and (11 + sum(computer_cards) > 21):
        new_computer_card = 1
    computer_cards.append(new_computer_card)

def is_bust(score):
    """Check if player score is over 21."""
    if score > 21:
        return True
    else:
        return False

def is_blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return True
    else:
        return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():

    player_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    if is_blackjack(player_cards):
        player_score = 0

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if player_score == 0:
        end_of_game( player_cards, player_score, computer_cards, computer_score)


    else:
        card_added = True
        while card_added:
            card_added = new_card_player(player_cards)
            if card_added:
                player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                if is_bust(player_score):
                    card_added = False

        while sum(computer_cards) < 17:
            new_card_computer(computer_cards)
            computer_score = sum(computer_cards)

        if is_blackjack(computer_cards):
            computer_score = 0

        end_of_game(player_cards,player_score, computer_cards, computer_score)

new_game = True
while new_game:
    new_game_choice = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    if new_game_choice == 'n':
        new_game = False
    else:
        print("\n" * 50)
        print(art.logo)
        blackjack()

