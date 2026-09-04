import random


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


def play_number_game(
	input_function=input,
	output_function=print,
	random_function=random.randint,
):
	"""Play a game where the player guesses a number from 1 through 100."""
	secret_number = random_function(1, 100)
	attempt_count = 0

	output_function("I picked a number from 1 to 100.")

	while True:
		guess_text = input_function("Enter your guess: ")

		try:
			guess = int(guess_text)
		except ValueError:
			output_function("Please enter a whole number.")
			continue

		attempt_count += 1

		if guess < secret_number:
			output_function("Higher!")
		elif guess > secret_number:
			output_function("Lower!")
		else:
			output_function(
				f"Correct! You guessed the number in {attempt_count} attempts."
			)
			return attempt_count


def play_word_game(
	input_function=input,
	output_function=print,
	choice_function=random.choice,
):
	"""Play a game where the player reveals a GitHub term one letter at a time."""
	secret_word = choice_function(GITHUB_TERMS).lower()
	guessed_letters = set()
	attempt_count = 0

	output_function("Guess the GitHub term one letter at a time.")

	while True:
		display_word = " ".join(
			letter if letter == " " or letter in guessed_letters else "_"
			for letter in secret_word
		)
		output_function(display_word)

		if all(letter == " " or letter in guessed_letters for letter in secret_word):
			output_function(
				f"Correct! The word was '{secret_word}' in {attempt_count} attempts."
			)
			return attempt_count

		guess = input_function("Enter a letter: ").strip().lower()
		if len(guess) != 1 or not guess.isalpha():
			output_function("Please enter one letter.")
			continue
		if guess in guessed_letters:
			output_function("You already guessed that letter.")
			continue

		guessed_letters.add(guess)
		attempt_count += 1
		if guess in secret_word:
			output_function("Good guess!")
		else:
			output_function("That letter is not in the word.")


def run_menu(input_function=input, output_function=print):
	"""Display the game menu until the player exits."""
	while True:
		output_function("\nGame Menu")
		output_function("1. Number guessing game")
		output_function("2. Word guessing game")
		output_function("3. Exit")
		choice = input_function("Select a game: ").strip()

		if choice == "1":
			play_number_game(
				input_function=input_function,
				output_function=output_function,
			)
		elif choice == "2":
			play_word_game(
				input_function=input_function,
				output_function=output_function,
			)
		elif choice == "3":
			output_function("Thanks for playing!")
			return
		else:
			output_function("Please select 1, 2, or 3.")


if __name__ == "__main__":
	run_menu()
