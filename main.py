'''
>>>> Codebreaker <<<<
El objetivo del juego es adivinar una secuencia numérica de 4 cifras
oculta por el oponente en el menor número de intentos posibles.
'''
from codebreaker import Codebreaker

INTENTOS_TOTALES = 10  # Constante que nos indica el numero maximo de itentos

codebreaker = Codebreaker()

intento = 0  # Contador de ciclos

# Lee el archivo de texto con las instrucciones
texto = Codebreaker.instrucciones('texto.txt')
print(texto)

truenumber = Codebreaker.generar()

while intento != INTENTOS_TOTALES:
    numero = input('Ingresa un numero Ej. (1234)   : ')
    resolve = codebreaker.adivinar(truenumber, numero)

    if resolve == 'Error':
        print("Error: El numero no se ajusta al formato solicitado")
    else:
        print("Tus aciertos son los siguentes :", resolve)

    if resolve == 'XXXX':
        print('Has Ganado, Felicitaciones !!')
        break

    intento += 1

print()
if intento == INTENTOS_TOTALES:
    print('Lo ciento has completado el maximo de intentos ')
    print('Sigue participando')
else:
    print('Con', intento + 1, 'Intento(s)')
