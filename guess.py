
from __future__ import annotations
from word import Word
from enum import Enum


class Guess(Word):
    def __init__(self: Guess, guess: str, word: Word) -> None:
        super().__init__(guess)
        
        self.__word = word
        self.__type = self.__get_type()

    def __get_type(self: Guess) -> GuessType:
        assert self.isalpha()

        if self.length == 1:
            return GuessType.letter

        elif self.length == self.__word.length:
            return GuessType.word

        raise ValueError
        
    @property
    def is_letter(self: Guess) -> bool:
        return self.__type == GuessType.letter


class GuessType(Enum):
    letter = 1
    word = 2