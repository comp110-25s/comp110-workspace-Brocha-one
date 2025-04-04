"""My very own Wordle program"""

__author__ = "730555924"

# comments key: * = received guidance in creating code, through Office hours TAs


def contains_char(word: str, letter: str) -> bool:
    """A function that compares the guess to the real word"""
    assert (
        len(letter) == 1
    ), f"len('{letter}') is not 1"  # basically makes sure there's only one letter
    index: int = 0  # 0 makes it start at the beginning of the word*
    while (
        len(word) != index and word[index] != letter
    ):  # runs through the word letter-by-letter*
        index += 1
    if index == len(word):  # describes if letter is present in str or not*
        return False
    else:
        return True


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """A function that describes correctness using colored emojis"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    full_guess: str = ""  # storage variable for each emoji*
    index: int = 0
    while index < len(guess):
        if (
            guess[index] != secret[index]
        ):  # compares letters of guess to letters of secret*
            if contains_char(word=secret, letter=guess[index]) is True:
                full_guess = full_guess + YELLOW_BOX
            else:
                full_guess = full_guess + WHITE_BOX
        else:
            full_guess = full_guess + GREEN_BOX
        index += 1
    return full_guess


def input_guess(expected: int) -> str:
    """A function that prompts the user to input a word"""
    guess = input(f"Enter a {expected} character word:")
    while (
        len(guess) != expected
    ):  # determines if the length of guess does not equal expected*
        guess = input(f"That wasn't {expected} chars! Try again:")
    return guess


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # variable that helps keep track of number of turns
    i_g_str: str = ""  # "i_g_str" stands for "input_guess_string"
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        i_g_str = input_guess(len(secret_word))
        print(
            emojified(guess=i_g_str, secret=secret_word)
        )  # combines emojified with main*
        if i_g_str == secret_word:
            print(f"You won in {turns}/6 turns!")
            return
        else:
            turns += (
                1  # makes sure that if incorrect guess, we move onto the next turn*
            )
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
