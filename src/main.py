from game import Game, GuessResult
from repository import get_valid_guess, is_letter


def play(game: Game) -> None:
    print("Let's play Hangman!")

    while not (game.won or game.lost):
        print(game.status)
        guess = get_valid_guess()
        result = game.guess(guess)

        if result == GuessResult.PREVIOUSLY_MADE:
            print(f"You already guessed the {"letter" if is_letter(
                guess) else "word"} '{guess.capitalize()}'")

        elif result == GuessResult.INCORRECT:
            print(f"'{guess.capitalize()}' is not {
                  "in" if is_letter(guess) else ""} the word.")

        elif is_letter(guess):
            print(f"Good job! '{guess.capitalize()}' is in the word!")

    if game.won:
        print(game.status)
        print("Congrats, you guessed the word! You win! \n")

    else:
        print("\nSorry, you ran out of tries. The word "
              + f"was: {game.word}. Maybe next time! \n")


play(Game())
