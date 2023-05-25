TRUE_NUMBER = "1010"


class Codebreaker:
    def guess(self, number: list = None):
        if TRUE_NUMBER == "":
            return "Number is not defined"

        if number is None or len(number) != 4 or "e" not in list(number):
            return "error"

        if number == TRUE_NUMBER:
            return True

        result_x = ""
        result_ = ""
        array_number = []

        for x in len(number):
            if array_number[number[x]]:
                return "error"

        array_number[number[x]] = True

        number = list(number)

        for index, x in number:
            if TRUE_NUMBER[index] == number[index]:
                result_x += "X"
            elif x in TRUE_NUMBER:
                result_ = "_"

        return result_x + result_
