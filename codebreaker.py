trueNumber = "1010"


class Codebreaker:
    """
    Clase que define un objeto juego
    """
    def adivinar(self, numero=None):
        """
        Función que evalúa la entrada por teclado del jugador
        Args:
        [numero: str]: cadena que define la entrada del jugador
        """
        if trueNumber == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4:
            return "error"

        if numero == trueNumber:
            return True

        resultado = ""
        numero = list(numero)

        for index, x in enumerate(numero):
            if trueNumber[index] == numero[index]:
                resultado += "X"

            elif x in trueNumber:
                resultado += "_"

        return resultado
