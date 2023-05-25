"""
This module contains the main function that runs the Codebreaker game.
It handles user input, provides user feedback, and controls the game
 loop.
"""
import logging

from codebreaker import Codebreaker
from core import logging_config
from core.decorators import with_logging

logging_config.setup_logging()
logger: logging.Logger = logging.getLogger(__name__)
TOTAL_TRIES: int = 10


@with_logging
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

    logger.info("Let's play Codebreaker!\nYou have %s attempts.", TOTAL_TRIES)

    while attempt < TOTAL_TRIES:
        attempt += 1
        number: str = input("Enter a 4 digit number: ")
        try:
            resolve: str = codebreaker.guess(number)
        except ValueError as error:
            logger.warning(error)
            continue
        logger.info(resolve)
        if resolve.count("X") == 4:
            logger.info("You win!!!")
            break

    if attempt == TOTAL_TRIES:
        logger.info("You have reached the maximum number of tries. You lost.")


if __name__ == "__main__":
    play_codebreaker()
