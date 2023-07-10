""" Main file for CodeBreaker
Little game where you must guess the secret number)"""

from codebreaker import CodeBreaker

TOTAL_TRIES = 10  # Amount of total tries (int)
tries = 0  # pylint: disable=C0103
# pylint false possitive: Constant name "tries" doesn't conform
# to UPPER_CASE naming style (invalid-name)

print('Play Codebreaker!')
print('-----------------')
print('10 tries!')

codebreaker = CodeBreaker()

while tries != TOTAL_TRIES:
    number = input('Number: ')
    resolve = codebreaker.guess_number(number)  # pylint: disable=C0103

    if resolve == 'WIN':
        print('YOU WIN!!!')
        break

    if 'Error' not in resolve:
        print(f'Result: "{resolve}"')

        tries += 1
        print(f'{TOTAL_TRIES-tries} tries remain...')
    else:
        print(resolve)
else:
    print('GAME OVER!!!')
