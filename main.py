from codebreaker import CodeBreaker

INTENTOS_TOTALES = 10
codebreaker = CodeBreaker()

intento = 0

print('Play Codebreaker!')

while intento != INTENTOS_TOTALES:

    number = input('Numero:').strip()
    resolve = codebreaker.adivinar(number)
    print(resolve)

    if resolve == True:
        print('You win!!')
        break

    intento += 1
