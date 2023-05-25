""" Class file for CodeBreaker"""
# __doc__ (Class for little game CodeBreaker where you must guess
# the secret number)

SECRET_NUMBER = '1010'  # SECRET NUMBER CONSTANT


class CodeBreaker:  # pylint: disable=too-few-public-methods
    """
    Class for guess the secret number

    Arguments:
    number (str)

    Insert a number with a input() function, instance the class, and
    if you get a 'type(resolve) == bool' and is True, print a win message,
    if not print the instance as 'print(resolve)'.

    >>> codebreaker = CodeBreaker()
    >>> resolve = codebreaker.guess_number(1010)
    True

    TODO:
        Make a refactor in MVC, add Exceptions and move main code
        inside the class

    """

    def __init__(self) -> None:
        """
        Init Function

        Arguments:
        self
        """

    @classmethod
    def guess_number(cls, number=None):
        """
        Function for guess the secret number

        Arguments:
        number (str)

        Returns X for guessed character or _ for character inside string.
        If you guess the secret number, returns a bolean value (True)

        >>> guess_number(1010)
        True

        TODO:
            Refactor the code and split in little functions.
        """
        if SECRET_NUMBER == '':
            return 'Number is not defined!'

        if number == SECRET_NUMBER:
            return True

        result = ''
        number = list(number)

        if number is None or len(number) != 4 or 'e' in list(number):
            return 'Error: Insert only 4 numbers!'

        for index, value in enumerate(number, start=0):
            if SECRET_NUMBER[index] == number[index]:
                result += 'X'
            else:
                if SECRET_NUMBER.find(value) != -1:
                    result += '_'
                else:
                    result += '?'

        return result
