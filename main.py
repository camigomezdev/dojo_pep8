"""This line of code import the class CodeBreaker """
from codebreaker import CodeBreaker

TOTAL_ATTEMPS = 10
codebreaker = CodeBreaker()
user_attemps = 0

print('\nPlay Codebreaker!\n')
print("*************************** GAME RULES ***************************\n"
      "1. You must enter a 4-digit number without duplicate digits\n"
      "2. You only have 10 attempts to win the game\n"
      "******************************************************************\n")

while user_attemps < TOTAL_ATTEMPS:
    user_number = input('Enter a number:')
    resolve = codebreaker.adivinar(user_number)
    if resolve == 1:
        print('You win!! Congrats!!')
        break

    print(resolve)
    user_attemps += 1
    if user_attemps == 10:
        print("Game Over :( !! You used your 10 available attemps")
