
from __future__ import annotations
from word import Word
from guess import Guess
from repository import get_random_word


class Game:
    __tries = 6
    __guessed_letters: list[str] = []
    __guessed_words: list[str] = []
    __current_status: str

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

        elif guess.is_word(self.word):
            return guess in self.__guessed_words

        raise ValueError("Guess must be a letter or word")

    def made_incorrect_guess(self: Game, guess: Guess) -> None:
        self.__tries -= 1

        if guess.is_letter:
            self.__guessed_letters.append(guess)
            
        elif guess.is_word(self.word):
            self.__guessed_words.append(guess)

        else:
            raise ValueError("Guess must be a letter or word")

    def made_correct_guess(self: Game, guess: Guess) -> None:
        if guess.is_letter:
            self.__guessed_letters.append(guess)
            self.__update_current_status(guess)

        elif guess.is_word(self.word):
            self.__current_status = self.__word

        else:
            raise ValueError("Guess must be a letter or word")        

    def __update_current_status(self: Game, guess: Guess) -> None:
        word_as_list = list(self.__current_status)

        indices = [i for i, letter in enumerate(self.__word) if letter == guess]

        for index in indices:
            word_as_list[index] = guess

        self.__current_status = "".join(word_as_list)

    @property
    def tries(self: Game) -> int:
        return self.__tries

    @property
    def current_status(self: Game) -> str:
        return self.__current_status

    @property
    def word(self: Game) -> Word:
        return self.__word
        