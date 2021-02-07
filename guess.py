
from __future__ import annotations
from word import Word
from enum import Enum


class Guess(Word):
    def __init__(self: Guess, guess: str, word: Word) -> None:
        super().__init__(guess)
        
        self.__word = word
        self.__validate_guess()

    def __validate_guess(self: Guess) -> None:
        if not self.isalpha():
            raise ValueError("\n" + "Not a valid guess" + "\n")

        elif self.length == 1:
            self.__type = GuessType.letter

        elif self.length == self.__word.length:
            self.__type = GuessType.word

        else:
            raise ValueError("\n" + "Guess must be a letter or word" + "\n")
        
    @property
    def is_letter(self: Guess) -> bool:
        return self.__type == GuessType.letter


class GuessType(Enum):
    letter = 1
    word = 2