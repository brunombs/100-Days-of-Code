import random
import hangman_words
import hangman_art
print(hangman_art.logo)
selected_word = random.choice(hangman_words.words)
display = []
guesses = 6
for l in selected_word:
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")
    if guess not in selected_word:
        guesses -= 1
    for p in range(len(selected_word)):
        letter = selected_word[p]
        if letter == guess:
            display[p] = letter
    print(display)
    print(hangman_art.stages[guesses])
    if "_" not in display:
        end_of_game = True
        print("You won.")
    if guesses > 1 and "_" in display:
        print(f"You still have {guesses} guesses left.")
    elif guesses == 1 and "_" in display:
        print(f"You still have {guesses} guess left.")
    if guesses == 0 and "_" in display:
        end_of_game = True
        print("You lost.")