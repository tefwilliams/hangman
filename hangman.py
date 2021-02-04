
from __future__ import annotations
from guess import Guess
from game import Game
from repository import display_hangman


def play(game: Game):
    print_starting_text(game)
    word = game.word

    while not game.won() or not game.lost():
        guess = Guess(input("Please guess a letter or word: "))

        if guess.is_valid:
            evaluate_guess(game, guess)

        else:
            print("Not a valid guess.")

        print(display_hangman(game.tries))
        print(game.current_status)
        print("\n")

    if game.won():
        print("Congrats, you guessed the word! You win!")

    else:
        print("Sorry, you ran out of tries. The word was: %s. Maybe next time!" %word)


def print_starting_text(game: Game):
    print("Let's play Hangman!")
    print(display_hangman(game.tries))
    print(game.current_status)
    print("\n")


def evaluate_guess(game: Game, guess: Guess) -> None:
    word = game.word

    if game.already_guessed(guess):
        print("You already guessed the letter", guess) if guess.is_letter else print("You already guessed the word", guess)

    elif guess not in word:
        print(guess, "is not in the word.") if guess.is_letter else print(guess, "is not the word.")
        game.made_incorrect_guess(guess)

    else:
        if guess.is_letter:
            print("Good job,", guess, "is in the word!") 

        game.made_correct_guess(guess)


play(Game())
