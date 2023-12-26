from enum import Enum
from repository import display_hangman, get_random_word, is_letter


class Game:
    __tries = 6
    __guesses = set()

    def __init__(self) -> None:
        self.__word = get_random_word().upper()

    @property
    def won(self):
        return "_" not in self.__current_status

    @property
    def lost(self) -> bool:
        return self.__tries == 0

    def guess(self, guess: str):
        if not guess.isalpha():
            raise ValueError("\nAll characters must be alphabetic")

        if guess.capitalize() in self.__guesses:
            return GuessResult.PREVIOUSLY_MADE

        self.__guesses.add(guess.upper())

        if not (
            guess.upper() in self.__word
            if is_letter(guess)
            else guess.upper() == self.__word
        ):
            self.__tries -= 1
            return GuessResult.INCORRECT

        return GuessResult.CORRECT

    @property
    def __current_status(self):
        if self.__word in self.__guesses:
            return self.__word

        return "".join(
            letter
            if letter in self.__guesses
            else "_"
            for letter in self.__word
        )

    @property
    def status(self):
        return f"""
{display_hangman(self.__tries)}

{self.__current_status}

{", ".join(sorted(self.__guesses))}
"""

    @property
    def word(self):
        return self.__word


class GuessResult(Enum):
    CORRECT = 0
    INCORRECT = 1
    PREVIOUSLY_MADE = 2
