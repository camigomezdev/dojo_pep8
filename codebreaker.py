"""
This module contains the mechanics of the Codebreaker game.
"""
import random
from typing import Optional

from core.decorators import with_logging, benchmark


class Codebreaker:
    """Class to represent the Codebreaker game"""

    def __init__(self) -> None:
        """
        Initialize a Codebreaker game by generating a random 4-digit
         number.
        """
        self.right_number: str = self._generate_random_number()

    @staticmethod
    @with_logging
    @benchmark
    def _generate_random_number() -> str:
        """
        Generate a 4-digit number string with non-repeating digits.
        :return: The generated 4-digit number
        :rtype: str
        """
        return "".join(random.sample("0123456789", 4))

    def _generate_feedback(self, guess: str) -> str:
        """
        Generate feedback for a given guess.
        :param guess: The guess to generate
        :type guess: str
        :return: The feedback string, containing "X" for each correct
         digit at the right position and "_" for each correct digit at
          the wrong position.
        :rtype: str
        """
        return "".join(
            "X" if guessed_digit == right_digit else "_" if
            guessed_digit in self.right_number else ""
            for guessed_digit, right_digit in zip(guess, self.right_number)
        )

    @with_logging
    def guess(self, guess: Optional[str] = None) -> str:
        """
        Handle a guess in the Codebreaker game and determines whether
         the guess is correct or not.
        :param guess: The guessed number. Defaults to None
        :type guess: str
        :return: "XXXX" if the guess is correct; otherwise, feedback on
         the guess
        :rtype: str
        """
        if guess is None or len(guess) != 4 or not guess.isdecimal() or\
                len(set(guess)) != 4:
            raise ValueError(
                "Invalid guess. Must be a 4-digit number with unique digits.")
        return self._generate_feedback(
            guess) if guess != self.right_number else "XXXX"
