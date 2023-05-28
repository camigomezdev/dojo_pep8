from codebreaker import Codebreaker

TOTAL_ATTEMPTS = 5
ATTEMPTS = 1
codebreaker = Codebreaker()


print('Jugar Codebreaker!')

while ATTEMPTS <= TOTAL_ATTEMPTS:
    number = input('Adivina el número de 4 cifras: ')
    resolve = codebreaker.adivinar(number)
    print(resolve)
    if resolve is True:
        print('You win!!')
        break
    ATTEMPTS += 1
