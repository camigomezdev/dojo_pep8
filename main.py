from codebreaker import Codebreaker

INTENTOS_TOTALES = 10
intento = 0
codebreaker = Codebreaker()

print('Jugar Codebreaker!')

while intento != INTENTOS_TOTALES:
    number = input('Numero: ')
    intento, resolve = codebreaker.adivinar(intento, number)

    if isinstance(resolve, bool) and resolve:
        print('You win!!')
        break
    elif isinstance(resolve, bool) and not resolve:
        print('Los números a adivinar no cumplen las condiciones\
               \nModificar código')
        break
    else:
        print(resolve)
        print(f'Intentos: {intento} de {INTENTOS_TOTALES}')

if intento == 10:
    print('No lo has logrado :(')
