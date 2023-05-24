"""
    This module defines the Codebreaker class. It imports the
    random Python module to generate digits randomly for the "right_number"
    variable.
"""
import random


class Codebreaker:
    """ This class defines the Codebreaker object. """

    def __init__(self):
        """
            This method initializes the "right_number" variable to a string
            converted from a 4 digit random number without repeated digits.
        """
        self.right_number = str(''.join(random.sample("0123456789", 4)))

    def guess(self, number=None):
        """
            This method takes two parameters, self and number (with a default
            value of None). It will test if the "number" entered by the user
            matches the class' "right_number" variable, and if not, return an
            "X" for each digit guessed correctly and in the right position,
            and "_" for each number order guessed correctly but in the wrong
            position.
        """

        if number is None or len(number) != 4 or not number.isdecimal():
            raise TypeError
        if number == self.right_number:
            return True

        ok_number_ok_position = ''
        ok_number_bad_position = ''
        found_digits = [False for i in range(10)]

        for digit in number:
            if found_digits[int(digit)]:
                raise ValueError
            found_digits[int(digit)] = True

        number = list(number)

        for index, digit in enumerate(number):
            if self.right_number[index] == number[index]:
                ok_number_ok_position += 'X'
            elif digit in self.right_number:
                ok_number_bad_position += '_'

        return ok_number_ok_position + ok_number_bad_position
