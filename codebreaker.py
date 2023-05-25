class Codebreaker:
    def __init__(self):
        self.TRUE_NUMBER = '1025'

    def adivinar(self, intento=0, numero=None):
        self.arrayNumber = []
        self.check_truenumber = 0

        # Verifico que se haya ingresado bien el número a adivinar
        # Si no se cumple cancelo la ejecución y doy aviso
        for i in self.TRUE_NUMBER:
            if self.TRUE_NUMBER.count(i) > 1:
                self.check_truenumber += 1

        if self.TRUE_NUMBER == '' or len(self.TRUE_NUMBER) != 4 \
           or not self.TRUE_NUMBER.isnumeric() or self.check_truenumber > 0:
            return 0, False

        # Verifico que se cumpla la consigna de ingresar 4 números
        if numero == '' or len(numero) != 4 or not numero.isnumeric():
            self.intento = intento  # No pierde un intento
            return self.intento, \
                'Se debe ingresar un número natural de 4 dígitos'

        # Verifico que se cumpla la consigna de digitos no repetidos
        for i in numero:
            if numero.count(i) > 1:
                self.intento = intento  # No pierde un intento
                return self.intento, 'No se deben ingresar números repetidos'

        # Proceso respuesta de acuerdo a lo ingresado
        if numero == self.TRUE_NUMBER:
            return intento, True
        else:
            self.intento = intento+1  # Pierde un intento
            for x in range(0, len(numero)):
                if numero[x] == self.TRUE_NUMBER[x]:
                    self.arrayNumber.append("_")
                elif numero[x] in self.TRUE_NUMBER:
                    self.arrayNumber.append("X")
                else:
                    self.arrayNumber.append("#")
            return self.intento, ''.join(self.arrayNumber)
