from __future__ import annotations

TRUE_NUMBER = "1427"


class CodeBreaker:
    def adivinar(self, numero=None):
        if TRUE_NUMBER == " ":
            return "Numero no esta definido"

        if numero is None or len(numero) != 4:
            return "error"
        if numero == TRUE_NUMBER:
            return True

        resultado = ""
        for i in range(len(TRUE_NUMBER)):
            if TRUE_NUMBER[i] == numero[i]:
                resultado += "x"
            elif numero[i] in TRUE_NUMBER and numero[i] not in resultado:
                resultado += "y"
            else:
                resultado += "-"
        return resultado
