
from __future__ import annotations
from word import Word


class Guess(Word):
    def __init__(self: Guess, guess: str, word: Word) -> None:
        super().__init__(guess)
        self.word = word

        assert self.isalpha()
        assert self.is_letter or self.is_word

    @property
    def is_letter(self: Guess) -> bool:
        return self.length == 1

    @property
    def is_word(self: Guess) -> bool:
        return self.length == self.word.length

