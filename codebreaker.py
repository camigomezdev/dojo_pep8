true_number = "1010"


class CodeBreaker:

    def guess(self, number=None):
        if not true_number:
            return 'Number is not defined'
        
        if not number or len(number) != 4:
            return "error"

        if number == true_number:
            return True

        resultX = ''
        result = ''
        array_number = []

        for x in len(number):
            if (array_number[number[x]]):
                return 'error'

            array_number[number[x]] = True

        number = list(number)

        for index, x in number:
            if true_number[index] == number[index]:
                resultX += 'X'

            elif x in true_number:
                result = '_'

        return resultX + result
