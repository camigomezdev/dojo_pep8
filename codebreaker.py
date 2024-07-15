'''inicio del programa'''

TRUENUMBER = "1111"

class Codebreaker:

    '''clase para adivinar un numero de 4 digitos'''

    def adivinar(self, numero=None):
        '''Aca debe llevar un docstring si no va un init'''
        if not TRUENUMBER:
            return 'Number is not defined'

        if numero is None or len(numero) != 4 or not numero.isdigit():
            return "error"

        if numero == TRUENUMBER:
            return True

        resultadox  = ''
        resultado  = ''
        arraynumber = [False] * 10 # Asumiendo que los numeros son de 0 al 9

        for x in numero:
            if arraynumber[int(x)]:
                return 'error'
            arraynumber[int(x)] = True

        for index, x in enumerate (numero):
            if TRUENUMBER[index] == x:
                resultadox+='X'
            elif x in TRUENUMBER:
                resultado+='_'


        return resultado+resultado
