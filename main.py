"""
This module contains the main function that runs the Codebreaker game.
It handles user input, provides user feedback, and controls the game
 loop.
"""
from codebreaker import Codebreaker

TOTAL_TRIES: int = 10


def play_codebreaker() -> None:
    """
    It initiates a game of Codebreaker and handles user input and
     feedback presentation.
    The game continues until the player correctly guesses the number or
     exhausts the total allowed tries.
    :return: None
    :rtype: NoneType
    """
    codebreaker: Codebreaker = Codebreaker()
    attempt: int = 0

    print("Let's play Codebreaker!")

    while attempt < TOTAL_TRIES:
        attempt += 1
        number: str = input("Enter a 4 digit number: ")
        try:
            resolve: str = codebreaker.guess(number)
        except ValueError as error:
            print(error)
            continue
        print(resolve)
        if resolve.count("X") == 4:
            print("You win!!!")
            break

    if attempt == TOTAL_TRIES:
        print("You have reached the maximum number of tries. You lost.")


if __name__ == "__main__":
    play_codebreaker()
