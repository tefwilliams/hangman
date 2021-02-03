
from __future__ import annotations
from guess import Guess
from repository import get_word


class Game:
    __tries = 6
    guessed_letters: list[str] = []
    guessed_words: list[str] = []

    def __init__(self: Game) -> None:
        self.word = get_word()
        self.current_status = '_' * self.word.length

    def won(self: Game) -> bool:
        return "_" not in self.current_status

    def lost(self: Game) -> bool:
        return self.__tries == 0

    def already_guessed(self: Game, guess: Guess) -> bool:
        if guess.is_valid_letter():
            return guess in self.guessed_letters

        return guess in self.guessed_words

    def made_incorrect_guess(self: Game, guess: Guess) -> None:
        self.__tries -= 1

        if guess.is_valid_letter():
            self.guessed_letters.append(guess)
            
        else:
            self.guessed_words.append(guess)

    def made_correct_guess(self: Game, guess: Guess) -> None:
        if guess.is_valid_letter():
            self.guessed_letters.append(guess)
            word_as_list = list(self.current_status)
            indices = [i for i, letter in enumerate(self.word) if letter == guess]

            for index in indices:
                word_as_list[index] = guess

            self.current_status = "".join(word_as_list)

        else:
            self.current_status = self.word

    def get_remaining_tries(self: Game) -> int:
        return self.__tries

    def get_current_status(self: Game) -> str:
        return self.current_status