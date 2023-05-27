import dataclasses

NUMERO_A_ADIVINAR = "2345"


@dataclasses.dataclass
class Codebreaker:
    """Esta clase contiene el metodo adivinar
    """
    numero_fallado: str
    numero_acertado: str

    def adivinar(self, numero_ingresado=None):
        """Metodo que evalua el numeor ingresado por el jugador para
        determinar si los números ingresados son correctos o estan contenidos
        dentro del numero a adivinar.

        Args:
            numero_ingresado (str, optional): Recibe el numero para tratar de
            adivinar el numero oculto. Defaults to None.

        Returns:
            bool: Retorna False si aun no encuentra el nuero y True cuando es
            encontrado
        """
        if NUMERO_A_ADIVINAR == '':
            print("El número no esta definido!")
            return False

        if numero_ingresado is None:
            print("Error, debe ingresar un número")
            return False

        if len(numero_ingresado) != 4:
            print("Error, el número debe ser de 4 digitos")
            return False

        if numero_ingresado == NUMERO_A_ADIVINAR:
            print(f"Adivinaste, el número es: {NUMERO_A_ADIVINAR}")
            return True

        resultado = ""

        for index, item in enumerate(numero_ingresado):
            if NUMERO_A_ADIVINAR[index] == item:
                resultado += self.numero_acertado
            elif item in NUMERO_A_ADIVINAR:
                resultado += self.numero_fallado
            else:
                resultado += " "

        print(resultado)
        return False
