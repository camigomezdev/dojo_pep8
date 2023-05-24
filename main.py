"""
    This module will import the Codebreaker module and ask the user to enter a
    4 digit number.
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
    try:
        result = codebreaker.guess(number)
    except ValueError:
        print("The number can't contain repeated digits!.")
    except TypeError:
        print("Please enter a 4 digit number!.")
    else:
        if not isinstance(result, str) and result:
            print('You won! Number of guesses:', guess_number)
            break
        print(f'Incorrect! You\'ve guessed {guess_number} times.')
        if len(result) > 0:
            print(f'Hint: {result}')
        guess_number += 1
