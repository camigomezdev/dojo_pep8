"""
    CodeBreaker
"""
TRUE_NUMBER = "1010"


class CodeBreaker:

    """
    CodeBreaker class
    """

    def adivinar(self, numero=None):
        """

        Args:
            numero ():

        Returns:

        """
        if TRUE_NUMBER == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4:
            return "error"

        if numero == TRUE_NUMBER:
            return True

        resultado_x = ""
        resultado_ = ""
        numero = []

        for index in enumerate(numero):
            if TRUE_NUMBER[index] == numero[index]:
                resultado_x += "X"

            elif numero[index] in TRUE_NUMBER:
                resultado_ += "_"

        return resultado_x + resultado_
