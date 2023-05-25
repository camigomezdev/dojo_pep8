TRUE_NUMBER = "1010"


class CodeBreaker:

    def adivinar(self, numero=None):
        if TRUE_NUMBER == '':
            return 'Number is not defined'

        if numero is None or len(numero) != 4:
            return "error"

        if numero == TRUE_NUMBER:
            return True

        caracter = ''
        array_number = []

        # for x in range(len(numero)):

        #     if array_number[numero[x]] == True:
        #         return 'error'

        #     array_number[numero[x]] = True

        # numero = list(numero)

        for num in range(len(numero)):
            # Realiza la búsqueda y compara uno a uno la posición del índice del 'TRUE_NUMBER'
            # con el del número ingresado.

            if TRUE_NUMBER[num] == numero[num]:
                caracter += 'X'

            elif numero[num] in TRUE_NUMBER:
                caracter += '_'
            else:
                caracter += ' '

        return f"'{caracter}'"
