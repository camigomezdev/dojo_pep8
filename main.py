from __future__ import annotations

from codebreaker import CodeBreaker
from codebreaker import TRUE_NUMBER

INTENTOS_TOTALES = 5

code_breaker = CodeBreaker()
contador = 0

print("Jugar Codebreaker!")

while contador != INTENTOS_TOTALES:
    number = input("Ingrese 4 numeros enteros consecutivos:")
    resolve = code_breaker.adivinar(number)

    while resolve is not True:
        number = input("Ingrese 4 numeros enteros consecutivos:")
        resolve = code_breaker.adivinar(number)
        contador = contador + 1
        restantes = INTENTOS_TOTALES - contador

        if restantes == 0:
            print("*Perdiste*")
            print(" Juego terminado")
            print(f"El valor a adivinar era {TRUE_NUMBER}")
            break

        if resolve:
            print(f"Lo lograste en el intento numero {contador}")
        else:
            print(f"Te quedan {restantes} intentos")

    print("*Ganaste, Adivinaste*")
    break
