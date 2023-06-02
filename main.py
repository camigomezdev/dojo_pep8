from codebreaker import Codebreaker

TOTAL_ATTEMPTS = 5
attempts = 1
codebreaker = Codebreaker()


print('Play Codebreaker!')

while attempts <= TOTAL_ATTEMPTS:
    try:
        number = input('Guess the four digit number: ')
        resolve = codebreaker.guess_number(number)
        print(resolve)
        if resolve is True:
            print('You win!!')
            break
        attempts += 1
    except ValueError:
        print('Number cant be empty or its length is incorrect')
