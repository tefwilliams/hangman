
import random
from word import Word
from guess import Guess


def get_valid_guess(word: Word) -> Guess:
    while True:
        try:
            return Guess(input("Please guess a letter or word: "), word)

        except (AssertionError, ValueError):
            print("\n" + "Not a valid guess" + "\n")
            

def get_random_word() -> Word:
    word = random.choice(word_list)
    return Word(word)


def display_hangman(tries: int) -> str:
    return game_stages[tries]


word_list = [
    "chimney",
    "toast",
    "pigeon",
    "provision",
    "harbor",
    "waiter",
    "tower",
    "huge",
    "progressive",
    "cafe",
    "fraud",
    "photocopy",
    "tune",
    "wage",
    "resident",
    "exchange",
    "mind",
    "funny",
    "distribute",
    "ghost",
    "priority",
    "mirror",
    "financial",
    "credibility",
    "complain",
    "lesson",
    "addition",
    "license",
    "area",
    "code",
    "literacy",
    "revenge",
    "column",
    "hospital",
    "shallow",
    "sample",
    "reptile",
    "tropical"
]


game_stages = [
        # final state: head, torso, both arms, and both legs
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,
        # head, torso, both arms, and one leg
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,
        # head, torso, and both arms
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,
        # head, torso, and one arm
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,
        # head and torso
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,
        # head
        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,
        # initial empty state
        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]
