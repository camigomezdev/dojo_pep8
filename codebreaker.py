"""
This module contains the mechanics of the Codebreaker game.
"""
from typing import Optional


class Codebreaker:
    """Class to represent the Codebreaker game"""

    def __init__(self) -> None:
        self.real_number: str = "1010"

    def guess(self, number: Optional[str] = None) -> str:
        """
        The guess method allows a player to guess the real_number and
        provides feedback on the guess.
        :param number: A string representing the number to guess. The
        default value is None
        :type number: Optional[str]
        :return: A string with the game result for this guess.
        :rtype: str
        """
        if not self.real_number:
            raise ValueError("Number is not defined")
        if number is None or len(number) != 4 or not number.isdigit():
            raise ValueError("Input must be a 4 digit number")
        encountered_digits: list[bool] = [False] * 10
        for digit_str in number:
            digit = int(digit_str)
            if encountered_digits[digit]:
                raise ValueError("Digits must not repeat")
            encountered_digits[digit] = True
        correct_position: list[str] = [
            "X" if self.real_number[i] == number[i] else "" for i in range(4)]
        incorrect_position: list[str] = [
            "_" if digit in self.real_number and correct_position[
                i] != "X" else "" for i, digit in enumerate(number)]
        return "".join(correct_position + incorrect_position)
