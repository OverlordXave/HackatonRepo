from src import number_game


def test_word_game_handles_incorrect_and_repeated_letters():
	guesses = iter(["x", "r", "r", "e", "p", "o"])
	messages = []

	attempt_count = number_game.play_word_game(
		input_function=lambda _: next(guesses),
		output_function=messages.append,
		choice_function=lambda _: "repo",
	)

	assert attempt_count == 5
	assert "_ _ _ _" in messages
	assert "That letter is not in the word." in messages
	assert "You already guessed that letter." in messages
	assert messages[-1] == "Correct! The word was 'repo' in 5 attempts."


def test_word_game_reveals_spaces_in_phrases():
	guesses = iter(["p", "u", "l", "r", "e", "q", "s", "t"])
	messages = []

	number_game.play_word_game(
		input_function=lambda _: next(guesses),
		output_function=messages.append,
		choice_function=lambda _: "pull request",
	)

	assert "_ _ _ _   _ _ _ _ _ _ _" in messages
	assert messages[-1] == "Correct! The word was 'pull request' in 8 attempts."


def test_menu_runs_selected_game_then_exits(monkeypatch):
	selections = iter(["2", "3"])
	messages = []
	played_games = []

	monkeypatch.setattr(
		number_game,
		"play_word_game",
		lambda **_: played_games.append("word"),
	)

	number_game.run_menu(
		input_function=lambda _: next(selections),
		output_function=messages.append,
	)

	assert played_games == ["word"]
	assert messages[-1] == "Thanks for playing!"