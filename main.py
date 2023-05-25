"""

Play CodeBreaker
"""

from codebreaker import CodeBreaker

INTENTO = 0
INTENTOS_TOTALES = 10

codebreaker = CodeBreaker()


print("Jugar Codebreaker!")

while INTENTO != INTENTOS_TOTALES:
    number = input("Numero:")
    resolve = codebreaker.adivinar(number)
    print(resolve)
    if resolve:
        print("You win!!")
        break
