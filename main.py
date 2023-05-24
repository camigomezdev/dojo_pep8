from codebreaker import CodeBreaker

intentos_totales = 10
codebreaker = CodeBreaker()

intento = 0

print('Jugar Codebreaker!')

while intento != intentos_totales:
    number = input('Numero:')
    resolve = codebreaker.guess(number)
    print(resolve)
    if resolve:
        print('You win!!')
        break
