""" Validations Model for CodeBreaker"""
# __doc__ (Validations Model file for little game CodeBreaker)
from app.models.errors import CodeBreackerErrors


class CodeBreackerValidation:
    """
    Class for Validations Model

    Arguments:
    None

    Validates the numbers.

    >>> validation = CodeBreackerValidation(lang, username)
    True

    TODO:
        -

    """

    def __init__(self, lang: object, username: str) -> str:
        """
        Class Init Function

        Arguments:
        self
        lang (object)
        username (str)

        Inits the class CodeBreackerValidation (str)

        TODO:
            -
        """
        self.lang = lang
        self.username = username

    def is_number(self, number: str) -> int:
        """
        Function to validate if are numbers

        Arguments:
        self
        number (str)

        Validates the 4 inserted are numbers (str)

        TODO:
            -
        """
        if number.isnumeric():  # pylint: disable=R1705
            return True
        else:
            CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_FOUR_NUMBERS"],
                self.username)
            return False

    def verify_number(self, number: str, secret=True) -> int:
        """
        Function to validate secret number in config file
        or typed number

        Arguments:
        self
        lang (object)
        secret (bool)

        Validates the secret and typed number in config file (str)

        TODO:
            -
        """

        if not number and secret:  # pylint: disable=R1705
            return CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_SECRET_EMPTY"],
                self.username)
        elif not number and not secret:
            return CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_NUMBER_EMPTY"],
                self.username)
        else:
            return number

    def to_list(self, number: str, secret=True) -> list:
        """
        Function to validate list() lenght

        Arguments:
        self
        number (str)
        secret (bool)

        Validates lenght in secret and typed lists() (str)

        TODO:
            -
        """
        number_list = list(number)
        if len(number_list) != 4 and secret:  # pylint: disable=R1705
            return CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_SECRET_LENGHT"],
                self.username)
        elif len(number_list) != 4 and not secret:
            return CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_NUMBER_LENGHT"].format(
                    number),
                self.username)
        else:
            return number_list
