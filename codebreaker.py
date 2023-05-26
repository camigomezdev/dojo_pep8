TRUE_NUMBER = "1489"


class CodeBreaker:

    def adivinar(self, numero=None):
        if TRUE_NUMBER == '':
            return 'Number is not defined'

        if numero is None or len(numero) != 4:
            return "Error: number must have 4 digits"

        if numero == TRUE_NUMBER:
            return True

        caracter = ''
        array_number = [1]

        # Evaluar si un número se repite se repite dentro de la secuencia
        for x in range((len(numero))):

            if numero[x] in array_number:
                return f"Error: you have already entered the number {numero[x]} in position {array_number.index(numero[x])}"

            array_number.append(numero[x])

        numero = list(numero)

        for num in range(len(numero)):
            # Realiza la búsqueda y compara uno a uno la posición del índice del 'TRUE_NUMBER'
            # con el del número ingresado.

            if TRUE_NUMBER[num] == numero[num]:
                caracter += 'X'

            elif numero[num] in TRUE_NUMBER:
                caracter += '_'
            else:
                caracter += ' '

        return caracter
