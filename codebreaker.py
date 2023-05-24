true_number = "1010"


class CodeBreaker:

    def guess(self, number=None):
        if not true_number:
            return 'Number is not defined'
        print(list(number))
        if number is None or number != 4 or 'e' not in list(number):
            return "error"

        if number == true_number:
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
            if true_number[index] == number[index]:
                resultX += 'X'

            elif x in true_number:
                result = '_'

        return resultX + result
