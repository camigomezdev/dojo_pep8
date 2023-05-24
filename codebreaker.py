trueNumber = "1010"


class CodeBreaker:

    def guess(self, number=None):
        if trueNumber == '':
            return 'Number is not defined'

        if number is None or number != 4 or 'e' not in list(number):
            return "error"

        if number == trueNumber:
            return True

        resultX = ''
        result = ''
        arrayNumber = []

        for x in len(number):
            if (arrayNumber[number[x]]):
                return 'error'

            arrayNumber[number[x]] = True

        number = list(number)

        for index, x in number:
            if trueNumber[index] == number[index]:
                resultX += 'X'

            elif x in trueNumber:
                result = '_'

        return resultX + result
