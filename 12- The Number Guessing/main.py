from art import logo
import random
print(logo)
score = 0

def guessing_game():
    global score
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        chances = 10
    elif difficulty == "hard":
        chances = 5
    else:
        print("Invalid option.")
        return

    number = random.randint(1, 100)
    guessed_correctly = False

    while chances != 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        chances -= 1

        if guess > number:
            if chances != 0:
                print("Too high, try again.")
        elif guess < number:
            if chances != 0:
                print("Too low, try again.")
        elif guess == number:
            print(f"That's it! The number is {number}")
            guessed_correctly = True
            score += 1
            break

    if not guessed_correctly:
        print(f"Game over. The number was {number}")
        score = 0

while True:
    guessing_game()
    print(f"Your score: {score}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

