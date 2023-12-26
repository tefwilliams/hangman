import random


def get_alpha_string(input_text: str):
    while True:
        try:
            output = input(input_text)

            if not output.isalpha():
                print("The input must be a letter or word.\n")
                continue

            return output

        except ValueError as e:
            print(e)


def get_valid_guess():
    return get_alpha_string("Please guess a letter or word: ")


def get_random_word():
    return random.choice(word_list)


def display_hangman(tries: int) -> str:
    return game_stages[tries]


def is_letter(guess: str):
    return len(guess) == 1


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
