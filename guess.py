
from __future__ import annotations
from word import Word


class Guess(Word):
    def __new__(cls: type[Guess], guess: str):
        return super().__new__(cls, guess)

    def is_valid_letter(self: Guess) -> bool:
        return self.length == 1 and self.isalpha()

    def is_valid_word(self: Guess, word: Word) -> bool:
        return self.length == word.length and self.isalpha()