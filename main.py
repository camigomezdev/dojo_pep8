""" Main file for CodeBreaker"""
# __doc__ (Main file for little game CodeBreaker where you must guess
# the secret number)

from codebreaker import CodeBreaker

TOTAL_TRIES = 10  # Amount of total tries (int)
TRIES = 0

print('Play Codebreaker!')
print('-----------------')
print('10 tries!')

codebreaker = CodeBreaker()

while TRIES != TOTAL_TRIES:
    number = input('Number: ')
    resolve = codebreaker.guess_number(number)

    if isinstance(resolve, bool) and resolve:
        print('YOU WIN!!!')
        break

    print(resolve)

    TRIES += 1
    print(f'{TOTAL_TRIES-TRIES} tries remain...')
else:
    print('GAME OVER!!!')
