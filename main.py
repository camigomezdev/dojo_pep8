from codebreaker import CodeBreaker

total_attempts = 10
codebreaker = CodeBreaker()

attempt = 0

print('Jugar Codebreaker!')

while attempt != total_attempts:
    number = input('Numero:')
    resolve = codebreaker.guess(number)
    print(resolve)
    if resolve:
        print('You win!!')
        break
