"""The file that is executed and in which the interaction with the
the user occurs.
"""

from codebreaker import Codebreaker

TOTAL_ATTEMPTS = 10
codebreaker = Codebreaker()

current_attempt = 0

print('Play Codebreaker!')

while current_attempt != TOTAL_ATTEMPTS:
    number = input('Number: ')
    resolve = codebreaker.guess_number(number)
    print(resolve)
    if resolve is True:
        print('You win!!')
        break
    current_attempt += 1
    print(f'You have {TOTAL_ATTEMPTS - current_attempt} attempts left')
