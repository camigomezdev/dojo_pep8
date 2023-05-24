from codebreaker import CodeBreaker

total_attempts = 10
codebreaker = CodeBreaker()

attempt = 0

print('Jugar Codebreaker!')

while attempt < total_attempts:
    """
    This loop allows the player to make attempts to guess the code.

    The player is prompted to enter a number, and the guess is evaluated using the CodeBreaker class.
    The loop continues until the player wins, exceeds the maximum attempts, or enters an invalid number.
    """

    print("Attempt number:", attempt + 1)
    number = input('Numero:')
    attempt += 1

    if not number:
        print("Please write a number")
        break

    resolve = codebreaker.guess(number)
    print(resolve)

    if resolve == True:
        print('You win!!')
        break
    elif resolve == 'error':
        print('Please input a number of 4 digits')
        break

