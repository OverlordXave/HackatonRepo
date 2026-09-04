"""A command-line number guessing game."""

import random
from collections.abc import Callable


MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100
GITHUB_TERMS = (
    "repository",
    "repo",
    "commit",
    "branch",
    "switch",
    "clone",
    "remote",
    "origin",
    "pull",
    "push",
    "merge",
    "tag",
    "pull request",
)


def play_game(
    secret_number: int | None = None,
    input_function: Callable[[str], str] = input,
    output_function: Callable[[str], None] = print,
) -> int:
    """Run one game and return the number of valid guesses used."""
    if secret_number is None:
        secret_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)

    guesses = 0
    output_function(
        f"I'm thinking of a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}."
    )

    while True:
        try:
            guess = int(input_function("Enter your guess: "))
        except ValueError:
            output_function("Please enter a whole number.")
            continue

        if not MINIMUM_NUMBER <= guess <= MAXIMUM_NUMBER:
            output_function(
                f"Choose a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}."
            )
            continue

        guesses += 1
        if guess < secret_number:
            output_function("Higher!")
        elif guess > secret_number:
            output_function("Lower!")
        else:
            output_function(f"Correct! You guessed it in {guesses} guesses.")
            return guesses


def play_word_game(
    secret_word: str | None = None,
    input_function: Callable[[str], str] = input,
    output_function: Callable[[str], None] = print,
) -> int:
    """Run a letter-by-letter GitHub word guessing game."""
    if secret_word is None:
        secret_word = random.choice(GITHUB_TERMS)

    secret_word = secret_word.lower()
    guessed_letters: set[str] = set()
    guesses = 0
    output_function("Guess the GitHub term one letter at a time.")

    while True:
        display_word = " ".join(
            letter if letter == " " or letter in guessed_letters else "_"
            for letter in secret_word
        )
        output_function(display_word)

        if all(letter == " " or letter in guessed_letters for letter in secret_word):
            output_function(f"Correct! The word was '{secret_word}'.")
            return guesses

        guess = input_function("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            output_function("Please enter one letter.")
            continue
        if guess in guessed_letters:
            output_function("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        guesses += 1
        if guess in secret_word:
            output_function("Good guess!")
        else:
            output_function("That letter is not in the word.")


def run_menu(
    input_function: Callable[[str], str] = input,
    output_function: Callable[[str], None] = print,
) -> None:
    """Show the game menu until the user chooses to exit."""
    while True:
        output_function("\nGame Menu")
        output_function("1. Number guessing game")
        output_function("2. Word guessing game")
        output_function("3. Exit")
        choice = input_function("Select a game: ").strip()

        if choice == "1":
            play_game(input_function=input_function, output_function=output_function)
        elif choice == "2":
            play_word_game(input_function=input_function, output_function=output_function)
        elif choice == "3":
            output_function("Thanks for playing!")
            return
        else:
            output_function("Please select 1, 2, or 3.")


def main() -> None:
    """Start the game menu from the command line."""
    run_menu()


if __name__ == "__main__":
    main()