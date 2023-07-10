""" Core Model for CodeBreaker"""
import random
from random import randint

from app.models.validations import CodeBreackerValidation


class CodeBreaker:
    """ Class for CodeBreaker Model """

    def __init__(self, lang: object, cfg: object,  # pylint: disable=R0913
                 number: str,  username: str, duplicates: bool) -> None:
        """
        Inits the class CodeBreaker (str)
        """
        self.lang = lang
        self.cfg = cfg
        self.validation = CodeBreackerValidation(lang, username)
        self.show_x_not_number = cfg.getboolean("OPTIONS", "USE_X_NOT_NUMBER")

        self.username = username
        self.number = number
        self.duplicates = duplicates
        self.secret_number = self._secret_number

    def challenge(self) -> str:
        """
        Returns X for guessed digit or _ for a digit inside number.
        """
        if self.validation.is_number(self.number):

            secret_number = self.validation.verify_number(
                self.secret_number, True)
            number = self.validation.verify_number(self.number, False)

            number_list = self.validation.to_list(number, False)

            if self.duplicates:
                return self._check_digit(number_list, secret_number)

            if self.validation.verify_repeated_digit(number) is None:
                return self._check_digit(number_list, secret_number)
        return None

    def update_number(self, number: str):
        """
        Updates the typed number (str)
        """
        self.number = number

    @property
    def is_winner(self) -> bool:
        """
        If you guess the secret number, returns a bolean value (True)
        """
        return self.number == self.secret_number

    @property
    def realnumber(self) -> str:
        """
        Returns the hidden secret number
        """
        return self.secret_number

    @property
    def _secret_number(self):
        """
        Returns the current secret number
        """
        if isinstance(self.cfg.getboolean("OPTIONS", "USE_RAMDOM_NUMBER"),
                      bool) and self.cfg.getboolean("OPTIONS",
                                                    "USE_RAMDOM_NUMBER"):
            if self.duplicates:
                return str(randint(0, 9999))

            return ''.join(map(str, random.sample(range(0, 9), 4)))

        return self.cfg["OPTIONS"]["SECRET_NUMBER"]

    def _check_digit(self, number: list, secret_number: str) -> str:
        """
        Returns the the guessed numbers, chars by chars giving X or _
        """
        result_value = ''

        if not isinstance(number, list):
            return number

        for key, value in enumerate(number, start=0):
            if secret_number[key] == value:
                if self.show_x_not_number:
                    result_value += 'X'
                else:
                    result_value += number[key]
            if secret_number[key] != value and value in secret_number:
                result_value += '_'
            if secret_number[key] != value and value not in secret_number:
                result_value += ' '

        return result_value
