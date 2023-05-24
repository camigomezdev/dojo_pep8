"""
    This module will import the Codebreaker module and ask the user to enter a
    4 digit number. It will give the user "GUESS_LIMIT" amount of tries to
    guess it.
"""

from codebreaker import Codebreaker

# pylint: disable-msg=C0103
codebreaker = Codebreaker()
guess_number = 1

print('Let\'s play Codebreaker!')

while True:
    number = input('Try to guess the 4 digit number (enter \'q\' to quit): ')
    if number == 'q':
        break
    result = codebreaker.guess(number)
    if not isinstance(result, str):
        if result:
            print('You won! Number of tries:', guess_number)
            break
        print('Please enter a 4 digit number!')
        print(f'You\'ve tried {guess_number} times.')
    else:
        print(f'Incorrect! You\'ve tried {guess_number} times.')
        if len(result) > 0:
            print(f'Hint: {result}')
    guess_number += 1
