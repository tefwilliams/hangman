
from __future__ import annotations


class Word(str):
    def __new__(cls: type[Word], word: str, *args) -> Word:
        return super().__new__(cls, word.upper())

    def __init__(self: Word, *args) -> None:
        self.__length = len(self)

    @property
    def length(self: Word) -> int:
        return self.__length
