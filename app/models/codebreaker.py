""" Core Model for CodeBreaker"""
# __doc__ (CodeBreaker Model file for little game CodeBreaker)
import random
from random import randint
from app.models.validations import CodeBreackerValidation


class CodeBreaker:
    """
    Class for CodeBreaker Model

    Arguments:
        self
        lang (object)
        cfg (object)
        number (str)
        username (str)
        duplicates (bool)

    Instance it to run the game.

    >>> validation = CodeBreackerValidation(lang, username)
    True

    TODO:
        -

    """

    def __init__(self, lang: object, cfg: object,  # pylint: disable=R0913
                 number: str,  username: str, duplicates: bool) -> None:
        """
        Class Init Function

        Arguments:
        self
        lang (object)
        cfg (object)
        number (str)
        username (str)
        duplicates (bool)

        Inits the class CodeBreaker (str)

        TODO:
            -
        """

        self.lang = lang
        self.cfg = cfg
        self.validation = CodeBreackerValidation(lang, username)
        self.show_x_not_number = cfg.getboolean("OPTIONS", "USE_X_NOT_NUMBER")

        self.username = username
        self.number = number

        if isinstance(cfg.getboolean("OPTIONS", "USE_RAMDOM_NUMBER"),
                      bool) and cfg.getboolean("OPTIONS", "USE_RAMDOM_NUMBER"):
            if duplicates:
                self.secret_number = str(randint(0, 9999))
            else:
                self.secret_number = ''.join(
                    map(str, random.sample(range(0, 9), 4)))
        else:
            self.secret_number = cfg["OPTIONS"]["SECRET_NUMBER"]

    def challenge(self) -> str:
        """
        Function for get Challenge

        Arguments:
        self

        Returns X (or number) for guessed character or _ for character
        inside string.
        If you guess the secret number, returns a bolean value (True)

        >>> codebreaker = CodeBreaker(self.lang,
        self.cfg, number, username, False)
        >>> challenge = codebreaker.challenge()
        True

        TODO:
            Refactor the code and split in little functions.
        """

        if self.validation.is_number(self.number):

            secret_number = self.validation.verify_number(
                self.secret_number, True)
            number = self.validation.verify_number(self.number, False)

            number_list = self.validation.to_list(number, False)
            return self._check_digit(number_list, secret_number)
        return None

    def update_number(self, number: str):
        """
        Function to update number

        Arguments:
        self
        number (str)

        Returns the update typed number (str)

        TODO:
            -
        """
        self.number = number

    @property
    def is_winner(self) -> bool:
        """
        Property to validate the match

        Arguments:
        self

        Returns True when secret number match (str)

        TODO:
            -
        """
        return self.number == self.secret_number

    @property
    def realnumber(self) -> str:
        """
        Property to get the secret number

        Arguments:
        self

        Returns the hidden secret number (str)

        TODO:
            -
        """
        return self.secret_number

    def _check_digit(self, number: list, secret_number: str) -> str:
        """
        Function to get the guessed chars

        Arguments:
        self
        number (str)
        secret_number (str)

        Returns the the guessed numbers, chars by chars using X, _ or ? (str)

        TODO:
            -
        """
        result_value = ''

        for index, value in enumerate(number, start=0):
            if secret_number[index] == number[index]:
                if self.show_x_not_number:
                    result_value += 'X'
                else:
                    result_value += number[index]
            else:
                if secret_number.find(value) != -1:
                    result_value += '_'
                else:
                    result_value += '?'

        return result_value
