
from __future__ import annotations
from word import Word


class Guess(Word):
    def __init__(self: Guess, guess: str) -> None:
        super().__init__(guess)
        self.__is_valid = self.isalpha()

    @property
    def is_letter(self: Guess) -> bool:
        return self.__is_valid and self.length == 1

    def is_word(self: Guess, word: Word) -> bool:
        return self.__is_valid and self.length == word.length

