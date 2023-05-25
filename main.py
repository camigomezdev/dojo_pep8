from __future__ import annotations

from .codebreaker import CodeBreaker

INTENTOS_TOTALES = 10

code_breaker = CodeBreaker()
intento = 0

print("Jugar Codebreaker!")

while intento != INTENTOS_TOTALES:
    number = input("Numero:")
    resolve = code_breaker.adivinar(number)

    print(resolve)

    if resolve:
        print("You win!!")
        break
