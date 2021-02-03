
from __future__ import annotations


class Word(str):
    def __new__(cls: type[Word], word: str):
        return super().__new__(cls, word.upper())

    def __init__(self: Word, word: str) -> None:
        self.length = len(self)
