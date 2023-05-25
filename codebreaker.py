from __future__ import annotations

TRUE_NUMBER = "1010"


class CodeBreaker:
    def adivinar(self, numero=None):
        if TRUE_NUMBER == " ":
            return "Number is not defined"

        if numero is None or len(numero) != 4 or "e" not in list(numero):
            return "error"
        if numero == TRUE_NUMBER:
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
            if TRUE_NUMBER[index] == numero[index]:
                resultadoX += "X"

            elif x in TRUE_NUMBER:
                resultado_ = "_"
                return resultadoX + resultado_
