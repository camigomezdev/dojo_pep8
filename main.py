"""Este es el archivo principal donde se controlara el comportamiento del
juego
"""
from codebreaker import Codebreaker

INTENTOS_TOTALES = 10
codebreaker = Codebreaker('X', '_')

intento = 0

print('Jugar Codebreaker!')

while intento != INTENTOS_TOTALES:
    print(f"Intento {intento + 1}")
    numero_ingresado = input('Número:')
    resuelto = codebreaker.adivinar(numero_ingresado)
    if resuelto:
        break

    intento += 1
