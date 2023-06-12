""" Errors Model for CodeBreaker"""
# __doc__ (Validations Model file for little game CodeBreaker)


class CodeBreackerErrors():  # pylint: disable=too-few-public-methods
    """
    Class for Errors Model

    Arguments:
    None

    Runs the App.

    >>> CodeBreackerErrors(
                self.lang["LANG"]["LANG_VALIDATION_FOUR_NUMBERS"],
                self.username)
    True

    TODO:
        -

    """

    def __init__(self, message: str, username: str) -> None:
        """
        Class Init Function

        Arguments:
        self
        message (str)
        username (str)

        Inits the class CodeBreackerErrors (str)

        TODO:
            -
        """

        self.username = username
        self.message = message  # pylint: disable=pointless-statement
        self.show()

    def show(self) -> str:
        """
        Function to show errors

        Arguments:
        self

        Prints formated texts of errors

        TODO:
            -
        """

        print((f'[CodeBreaker] {self.username}: {self.message}'))

        return False
