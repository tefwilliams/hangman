
from __future__ import annotations
from word import Word


class Guess(Word):
    def __init__(self: Guess, guess: str) -> None:
        super().__init__(guess)

        self.__is_letter = self.length == 1
        self.__is_valid = self.isalpha()

    @property
    def is_letter(self: Guess) -> bool:
        return self.__is_letter

    @property
    def is_valid(self: Guess) -> bool:
        return self.__is_valid

