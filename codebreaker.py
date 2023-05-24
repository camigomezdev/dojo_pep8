"""
    This module defines the Codebreaker class, which has a single method
    called "guess"
"""

RIGHT_NUMBER = "1023"


class Codebreaker:
    """
        This class defines the Codebreaker object, and contains only one method
        named "guess"
    """

    def guess(self, number=None):
        """
            This method takes two parameters, self and number (with a default
            value of None). It will test if the "number" entered by the user
            matches the "RIGHT_NUMBER" constant, and if not, return an "X" for
            each number guessed correctly and in the right position, and "_"
            for each number order guessed correctly but in the wrong position.
        """

        if number is None or len(number) != 4 or not number.isnumeric():
            return False
        if number == RIGHT_NUMBER:
            return True

        ok_number_ok_position = ''
        ok_number_bad_position = ''

        number = list(number)

        for index, digit in enumerate(number):
            if RIGHT_NUMBER[index] == number[index]:
                ok_number_ok_position += 'X'
            elif digit in RIGHT_NUMBER:
                ok_number_bad_position += '_'

        return ok_number_ok_position + ok_number_bad_position
