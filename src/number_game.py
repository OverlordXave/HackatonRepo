import random


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


if __name__ == "__main__":
	play_number_game()
