"""
Implementation of Code Breaker game
"""

import string
from enum import Enum
from random import random


class CodeBreakerStatus(str, Enum):
    """
    Result constants
    """
    CORRECT_AND_POSITIONED = "X"
    CORRECT_AND_NOT_POSITIONED = "_"
    INCORRECT = "#"


class BadType(Exception): pass


class BadLength(Exception): pass


class BadFormat(Exception): pass


class RepeatedDigit(Exception): pass


class InvalidTrueNumber(Exception): pass


class CodeBreaker:
    """
    CodeBreaker is a game of guessing a secret number
    """

    def __init__(self):
        self.__SECRET_NUMBER = "".join(random.sample(string.digits, 4))

    def guess(self, number: str = None) -> str | bool:
        """
        Try to guess self.__TRUE_NUMBER with given param
        Args:
            number(str): 4 length number
        Return:
            bool: if the number is equal to self.__TRUE_NUMBER
            str: if number is valid but not equal to self.__TRUE_NUMBER
        """

        # Do validations to number
        if number is None or not isinstance(number, str):
            raise BadType("Param must be a str type")
        if len(number) != 4:
            raise BadLength("Param must be a 4 length str")
        if not number.isdigit():
            raise BadFormat("Param must be a str typed digit")

        if number == self.__SECRET_NUMBER:
            return True

        # Check if a number is repeated
        if any(number.count(char) > 1 for char in number):
            raise RepeatedDigit("Can't repeat number")

        result: str = ""

        # Check number
        for index, num in enumerate(number):
            if num == self.__SECRET_NUMBER[index]:
                result += CodeBreakerStatus.CORRECT_AND_POSITIONED
            elif num in self.__SECRET_NUMBER:
                result += CodeBreakerStatus.CORRECT_AND_NOT_POSITIONED
            else:
                result += CodeBreakerStatus.INCORRECT

        return result
