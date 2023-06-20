
TRUE_NUMBER = "8921"


class CodeBreaker:

    def guess(self, number=None):
        RESULT_X = 'X'
        RESULT__ = '_'
        number = list(number)
        array_number = ["0", "0", "0", "0"]

        if (
            TRUE_NUMBER == '' or
            len(TRUE_NUMBER) != 4 or
                len(set(TRUE_NUMBER)) != 4):

            return 'True Number is not well defined'

        if number is None or len(number) != 4 or len(set(number)) != 4:
            return "The number ingresed not fulfil the game's rules"

        if "".join(number) == TRUE_NUMBER:
            return True

        for index, x in enumerate(number):
            if TRUE_NUMBER[index] == number[index]:
                array_number[index] = RESULT_X

            elif x in TRUE_NUMBER:
                array_number[index] = RESULT__

        return "".join(array_number)
