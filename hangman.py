
from __future__ import annotations
from repository import get_word, game_stages


class Word(str):
    __tries = 6
    __guessed_letters: list[str] = []
    __guessed_words: list[str] = []

    def __new__(cls):
        word = get_word()
        return super().__new__(cls, word)

    def __init__(self: Word) -> None:
        self.__word_completion = '_' * len(self)
        self.length = len(self)

    def guessed(self: Word) -> bool:
        return "_" not in self.__word_completion

    def out_of_guesses(self: Word) -> bool:
        return self.__tries == 0

    def has_already_been_guessed(self: Word, guess: str) -> bool:
        if len(guess) > 1:
            return guess in self.__guessed_words

        return guess in self.__guessed_letters

    def get_remaining_tries(self) -> int:
        return self.__tries


def is_valid_letter(guess: str) -> bool:
    return len(guess) == 1 and guess.isalpha()


def is_valid_word(guess: str, word: Word) -> bool:
    return len(guess) == word.length and guess.isalpha()


def play(word: Word):
    print_starting_text(word)

    while not word.guessed() and not word.out_of_guesses():
        guess = input("Please guess a letter or word: ").upper()

        if is_valid_letter(guess):
            if word.has_already_been_guessed(guess):
                print("You already guessed the letter", guess)

            elif guess not in word:
                print(guess, "is not in the word.")
                word.__tries -= 1
                word.__guessed_letters.append(guess)

            else:
                print("Good job,", guess, "is in the word!")
                word.__guessed_letters.append(guess)
                word_as_list = list(word.__word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                word.__word_completion = "".join(word_as_list)

        elif is_valid_word(guess, word):
            if word.has_already_been_guessed(guess):
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                word.__tries -= 1
                word.__guessed_words.append(guess)

            else:
                word.__word_completion = word
        else:
            print("Not a valid guess.")

        print(display_hangman(word.__tries))
        print(word.__word_completion)
        print("\n")

    if word.guessed():
        print("Congrats, you guessed the word! You win!")

    else:
        print("Sorry, you ran out of tries. The word was: %s. Maybe next time!" %word)


def print_starting_text(word: Word):
    print("Let's play Hangman!")
    print(display_hangman(word.__tries))
    print(word.__word_completion)
    print("\n")


def display_hangman(tries: int) -> str:
    return game_stages[tries]

word = Word()
play(word)
