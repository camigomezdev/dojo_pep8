from codebreaker import CodeBreaker

TOTAL_TRIES = 10
code_breaker = CodeBreaker()

tries = 0

print("Let's play Codebreaker!")

while tries != TOTAL_TRIES:

    number = input('Number:')
    resolve = code_breaker.guess(number)

    if resolve is True:

        print('You win!!')
        break

    else:

        print(resolve)
        tries += 1
