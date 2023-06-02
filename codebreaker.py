NUMBER_TO_GUESS = '1356'


class Codebreaker:

    def guess_number(self, number: str = None) -> bool:
        """Attempts to guess a number entered and returns a result.

        Args:
            number (str optional): Number you want to guess. Defaults to None.

        Returns:
            bool: Returns True if the guessed number is correct.
                            Returns a string indicating the correctness of
                            each digit with 'X' representing a correct digit
                            in the correct position, and '_' representing a
                            correct digit in the wrong position.
                            Returns an error message if the number is not
                            valid or the number to guess is not defined.
        Raises:
            ValueError: Innapropiate argument value
        """
        if NUMBER_TO_GUESS == '':
            raise ValueError

        if number is None or len(number) != 4:
            raise ValueError

        if number == NUMBER_TO_GUESS:
            return True

        result_track_correct = ''
        result_track_incorrect = ''

        for idx in range(len(NUMBER_TO_GUESS)):
            if (number[idx] == NUMBER_TO_GUESS[idx]):
                result_track_correct += 'X'
            elif number[idx] in NUMBER_TO_GUESS:
                result_track_incorrect += '_'
        return result_track_correct + result_track_incorrect
