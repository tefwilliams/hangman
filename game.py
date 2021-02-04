
from __future__ import annotations
from guess import Guess
from repository import get_random_word


class Game:
    __tries = 6
    __guessed_letters: list[str] = []
    __guessed_words: list[str] = []

    def __init__(self: Game) -> None:
        self.__word = get_random_word()
        self.__current_status = '_' * self.__word.length

    def won(self: Game) -> bool:
        return "_" not in self.__current_status

    def lost(self: Game) -> bool:
        return self.__tries == 0

    def already_guessed(self: Game, guess: Guess) -> bool:
        if guess.is_letter:
            return guess in self.__guessed_letters

        return guess in self.__guessed_words

    def made_incorrect_guess(self: Game, guess: Guess) -> None:
        self.__tries -= 1

        self.__guessed_letters.append(guess) if guess.is_letter else self.__guessed_words.append(guess)

    def made_correct_guess(self: Game, guess: Guess) -> None:
        if guess.is_letter:
            self.__guessed_letters.append(guess)
            word_as_list = list(self.__current_status)
            indices = [i for i, letter in enumerate(self.__word) if letter == guess]

            for index in indices:
                word_as_list[index] = guess

            self.__current_status = "".join(word_as_list)

        else:
            self.__current_status = self.__word

    @property
    def tries(self: Game) -> int:
        return self.__tries

    @property
    def current_status(self: Game) -> str:
        return self.__current_status

    @property
    def word(self: Game) -> str:
        return self.__word