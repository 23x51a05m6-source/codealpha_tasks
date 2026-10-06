import random

WORDS = ["python", "computer", "programming", "hangman", "developer"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            print("Remaining attempts:", MAX_WRONG_GUESSES - wrong_guesses, "\n")

    print("Game Over!")
    print("The word was:", word)


if __name__ == "__main__":
    play_hangman()
