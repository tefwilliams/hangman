
from __future__ import annotations
from guess import Guess
from game import Game
from repository import game_stages


def play(game: Game):
    print_starting_text(game)
    word = game.word

    while not game.won() and not game.lost():
        guess = Guess(input("Please guess a letter or word: "))

        if guess.is_valid_letter():
            if game.already_guessed(guess):
                print("You already guessed the letter", guess)

            elif guess not in word:
                print(guess, "is not in the word.")
                game.made_incorrect_guess(guess)

            else:
                print("Good job,", guess, "is in the word!")
                game.made_correct_guess(guess)


        elif guess.is_valid_word(word):
            if game.already_guessed(guess):
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                game.made_incorrect_guess(guess)

            else:
                game.made_correct_guess(guess)
        else:
            print("Not a valid guess.")

        print(display_hangman(game.get_remaining_tries()))
        print(game.get_current_status())
        print("\n")

    if game.won():
        print("Congrats, you guessed the word! You win!")

    else:
        print("Sorry, you ran out of tries. The word was: %s. Maybe next time!" %word)


def print_starting_text(game: Game):
    print("Let's play Hangman!")
    print(display_hangman(game.get_remaining_tries()))
    print(game.get_current_status())
    print("\n")


def display_hangman(tries: int) -> str:
    return game_stages[tries]

game = Game()
play(game)
