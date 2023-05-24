trueNumber = "1010"


class CodeBreaker:

    def guess(self, number=None):
        if trueNumber == '':
            return 'Number is not defined'

        if number is None or len(number) != 4 or 'e' not in list(number):
            return "error"

        if number == trueNumber:
            return True

        resultadoX = ''
        resultado = ''
        arrayNumber = []

        for x in len(number):
            if (arrayNumber[number[x]]):
                return 'error'

            arrayNumber[number[x]] = True

        number = list(number)

        for index, x in number:
            if trueNumber[index] == number[index]:
                resultadoX += 'X'

            elif x in trueNumber:
                resultado = '_'

        return resultadoX + resultado
