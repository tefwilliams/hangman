
import random
from word import Word


def get_random_word() -> Word:
    word = random.choice(word_list)
    return Word(word)


def display_hangman(tries: int) -> str:
    return game_stages[tries]


word_list: list[str] = [
    "company",
    "minister",
    "scrawny",
    "weak",
    "gather",
    "friction",
    "gaudy",
    "plan",
    "sweater",
    "clumsy",
    "stain",
    "hour",
    "cover",
    "lunchroom",
    "elfin",
    "six",
    "quixotic",
    "groomed",
    "cheese",
    "hurried",
    "wasteful",
    "torpid",
    "pig",
    "voracious",
    "short",
    "hilarious",
    "title",
    "sweltering",
    "aboriginal",
    "scarce"
]


game_stages: list[str] = [
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