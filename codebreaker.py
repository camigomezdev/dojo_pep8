trueNumber = "1010"


class Codebreaker:
    def adivinar(self, numero=None):
        if trueNumber == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4 or "e" not in list(numero):
            return "error"

        if numero == trueNumber:
            return True

        resultadoX = ""
        resultado_ = ""
        arrayNumber = []

        for x in len(numero):
            if arrayNumber[numero[x]]:
                return "error"

            arrayNumber[numero[x]] = True

        numero = list(numero)

        for index, x in numero:
            if trueNumber[index] == numero[index]:
                resultadoX += "X"

            elif x in trueNumber:
                resultado_ = "_"

        return resultadoX + resultado_
