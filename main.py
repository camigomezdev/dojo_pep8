from codebreaker import Codebreaker

intentos_totales = 10
codebreaker = Codebreaker()

intento = 0

print("Jugar Codebreaker!")

while intento != intentos_totales:
    number = input("Numero:")
    resolve = codebreaker.adivinar(number)
    print(resolve)
    if resolve is True:
        print("You win!!")
        break
    intento += 1
