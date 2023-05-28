"""
Play to Code Breaker game
"""
import sys

from code_breaker import BadFormat
from code_breaker import BadLength
from code_breaker import BadType
from code_breaker import CodeBreaker
from code_breaker import CodeBreakerStatus
from code_breaker import RepeatedDigit

MAX_TRIES = 10
code_breaker = CodeBreaker()

TRY_COUNT = 0

print('Lets play Code Breaker!')
print('Rules:')
print('\t', CodeBreakerStatus.CORRECT_AND_POSITIONED.value, "=> Correct and well positioned")
print('\t', CodeBreakerStatus.CORRECT_AND_NOT_POSITIONED.value, "=> Correct and bad positioned")
print('\t', CodeBreakerStatus.INCORRECT.value, "=> Incorrect")

while TRY_COUNT <= MAX_TRIES:
    number = input('Guess the number:')
    try:
        result = code_breaker.guess(number)
        TRY_COUNT += 1
        if result is True:
            print('You win!! 🥳')
            sys.exit(0)
        else:
            print("Try again:", result)
    except BadType:
        print("Please enter a string")
    except BadLength:
        print("Please enter a 4 length number")
    except BadFormat:
        print("Please enter 4 digits")
    except RepeatedDigit:
        print("Please don't repeat digits")

print("You lose 😝")
