""" Class file for CodeBreaker """

SECRET_NUMBER = '1058'  # SECRET NUMBER CONSTANT


class CodeBreaker:  # pylint: disable=too-few-public-methods
    """
    Class for guess the secret number
    Insert a number with an input() function, instance the class like
    resolve = codebreaker.guess_number(number) and if you get
    a 'resolve == 'WIN', prints a win message,
    if not prints the instance as 'print(resolve)'.
    """

    @classmethod
    def guess_number(cls, number=None):
        """
        Returns X for guessed character or _ for character inside string.
        If you guess the secret number, returns a WIN string
        """
        if SECRET_NUMBER == '':
            return 'Number is not defined!'

        if number == SECRET_NUMBER:
            return 'WIN'

        result = ''
        repeated_numbers = {}
        number = list(number)

        if number is None or len(number) != 4 or 'e' in list(number):
            return 'Error: Insert only 4 numbers!'

        for digit in number:
            if digit in repeated_numbers:
                repeated_numbers[digit] += 1
            else:
                repeated_numbers[digit] = 0

        repeated_numbers = {k: v for k, v in repeated_numbers.items() if v > 0}

        if len(repeated_numbers) >= 1:
            return 'Error: No repeated numbers allowed!'

        for key, value in enumerate(number, start=0):
            if SECRET_NUMBER[key] == value:
                result += 'X'
            if SECRET_NUMBER[key] != value and value in SECRET_NUMBER:
                result += '_'
            if SECRET_NUMBER[key] != value and value not in SECRET_NUMBER:
                result += ' '

        return result
