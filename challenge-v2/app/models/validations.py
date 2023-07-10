""" Validations Model for CodeBreaker"""
from app.models.errors import CodeBreackerErrors


class CodeBreackerValidation:
    """ CodeBreacker Validation Class """

    def __init__(self, lang: object, username: str) -> None:
        """
        Inits the class CodeBreacker Validation
        """
        self.lang = lang
        self.username = username
        self.errors = CodeBreackerErrors()

    def is_number(self, number: str) -> bool:
        """
        Validates the 4 digits inserted are numbers
        """
        if number.isnumeric():  # pylint: disable=R1705
            return True
        else:
            self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_FOUR_NUMBERS"],
                self.username)
            return False

    def verify_number(self, number: str, secret=True) -> str:
        """
        Validates the secret and typed number in config file
        """
        if not number and secret:  # pylint: disable=R1705
            return self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_SECRET_EMPTY"],
                self.username)
        elif not number and not secret:
            return self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_NUMBER_EMPTY"],
                self.username)
        else:
            return number

    def verify_repeated_digit(self, number: str) -> str:
        """
        Checks if is a digit of given number are repeated (str)
        """
        repeated_numbers = {}

        for digit in number:
            if digit in repeated_numbers:
                repeated_numbers[digit] += 1
            else:
                repeated_numbers[digit] = 0

        repeated_numbers = {k: v for k, v in repeated_numbers.items() if v > 0}

        if len(repeated_numbers) >= 1:
            return self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_DUPLICATED_DIGITS"],
                self.username)

        return None

    def to_list(self, number: str, secret=True) -> list:
        """
        Validates lenght in secret and typed lists()
        """
        number_list = list(number)
        if len(number_list) != 4 and secret:  # pylint: disable=R1705
            return self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_SECRET_LENGHT"],
                self.username)
        elif len(number_list) != 4 and not secret:
            return self.errors.show(
                self.lang["LANG"]["LANG_VALIDATION_NUMBER_LENGHT"].format(
                    number),
                self.username)
        else:
            return number_list
