from typing import Union
NUMBER_TO_GUESS = '1356'


class Codebreaker:

    def adivinar(self, number: str = None) -> Union[bool, str]:
        """Attempts to guess a number entered and returns a result.

        Args:
            number (str optional): Number you want to guess. Defaults to None.

        Returns:
            Union[bool, str]: Returns True if the guessed number is correct.
                            Returns a string indicating the correctness of
                            each digit with 'X' representing a correct digit
                            in the correct position, and '_' representing a
                            correct digit in the wrong position.
                            Returns an error message if the number is not
                            valid or the number to guess is not defined.
        """
        if NUMBER_TO_GUESS == '':
            return 'Number to guess is not defined'

        if number is None or len(number) != 4:
            return 'Number is empty or length of numbers is wrong'

        if number == NUMBER_TO_GUESS:
            return True

        resultTrack = ''

        for idx in range(len(NUMBER_TO_GUESS)):
            if (number[idx] == NUMBER_TO_GUESS[idx]):
                resultTrack += 'X'
            elif number[idx] in NUMBER_TO_GUESS:
                resultTrack += '_'
            else:
                resultTrack += '#'

        return resultTrack
