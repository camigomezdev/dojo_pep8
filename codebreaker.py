"""Codebreaker module: the core of the game"""

TRUE_NUMBER = "7329"


class Codebreaker:
    """ A class that represents a match of the game and the rules to follow.
    """

    def guess_number(self, number=None):
        """Compares the number given by the player with the number to be 
        guessed and indicates the result of the player's guess. 

        Args:
            number (str, optional): A four digit number in string format. 
                                    Defaults to None.

        Returns:
            str or bool: A string describing the result of the guess if 
                        the answer is wrong. "True" is the answer is right.
        """

        if TRUE_NUMBER == '':
            return 'Number is not defined'

        if number is None or len(number) != 4:
            return "error"

        for digit in number:
            if digit not in "0123456789":
                return "error"

        if number == TRUE_NUMBER:
            return True

        accurate_position = ''
        wrong_position = ''
        validated_digits = []

        for digit in number:
            if digit in validated_digits:
                return 'error'
            validated_digits.append(digit)

        number = list(number)

        for index, digit in enumerate(number):
            if TRUE_NUMBER[index] == number[index]:
                accurate_position += 'X'

            elif digit in TRUE_NUMBER:
                wrong_position += '_'

        return accurate_position + wrong_position
