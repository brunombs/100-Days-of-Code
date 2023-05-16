from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose, you went over 21."

    if user_score == computer_score:
        return "That is a draw."
    elif computer_score == 0:
        return "You lose, your opponent has Blackjack."
    elif user_score == 0:
        return "You win with a Blackjack."
    elif user_score > 21:
        return "You lose, you went over 21."
    elif computer_score > 21:
        return "You win, your opponent went over 21."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def blackjack():
    print(logo)
    user = []
    computer = []
    continue_playing = True

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while continue_playing:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"    Your cards: {user[0]} and {user[1]}, total: {user_score}")
        print(f"    The first card of the computer is: {computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_playing = False
        else:
            new_card = str(input("Type 'y' to get another card, type 'n' to pass: "))
            if new_card == "y":
                user.append(deal_card())
            else:
                continue_playing = False

        while computer_score != 0 and computer_score < 17:
            print("[...Computer picking another number...]")
            computer.append(deal_card())
            computer_score = calculate_score(computer)

    if user_score <= 21:
        print(f"   Your final hand: {user}, final score: {user_score}")
    print(f"   Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")) != "n":
    blackjack()
