from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_number():
    return random.choice(cards)


def blackjack():
    user = [random_number(), random_number()]
    computer = [random_number(), random_number()]
    user_value = 0
    computer_value = 0
    continue_playing = True

    for card in user:
        user_value += card

    for card in computer:
        computer_value += card

    while continue_playing:

        # check if computer has 21 or more.
        if computer_value == 21 or computer_value > 21:
            if computer_value > 21:
                print(f"Computer lose with {computer_value} and user win with {user_value}")
                break
            print(f"Computer win with {computer_value} and you lose with {user_value}")
            continue_playing = False
            break

        # check if user has 21 or more.
        elif user_value == 21 or user_value > 21:
            if user_value > 21:
                print(f"You lose with {user_value} and computer with {computer_value}")
                break
            print(f"You win with {user_value} and computer lose with {computer_value}")
            break

        # show user cards
        print(f"    Yours cards: {user[0]} and {user[1]}, total: {user_value}")

        # show computer first card
        print(f"    The first card of the computer is: {computer[0]}")

        # check if user wants one more card
        new_card = str(input("Type 'y' to get another card, type 'n' to pass: "))
        if new_card == "n":
            # check if computer value is <= 16
            while computer_value < 16:
                print("[...Computer picking another number...]")
                new_number = random_number()
                computer_value += new_number
                print(f"Computer new number: {new_number}")

            # check if it is a draw.
            if computer_value == user_value:
                print(f"That is a draw, both have {user_value}")
                continue_playing = False

            if computer_value > 21:
                print(f"You win with {user_value} and computer lose with {computer_value}")
            elif computer_value > user_value:
                print(f"Computer win with {computer_value} and you lose with {user_value}")
                continue_playing = False
            elif user_value > computer_value:
                print(f"You win with {user_value} and computer lose with {computer_value}")
                continue_playing = False
        elif new_card == "y":
            user_value += random_number()
            computer_value += random_number()


play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
if play == "n":
    play = False

while play:
    print(logo)
    blackjack()
    play_again = str(input("Do you want to play again? Type 'y' or 'n': "))
    if play_again != 'y':
        play = False
