from codebreaker import Codebreaker

total_attempts = 10
codebreaker = Codebreaker()

attempt = 0

print('Play Codebreaker!')

while attempt != total_attempts:
   number = input('Number:')
   resolve = codebreaker.guess(number)
   print(resolve)
   if resolve == True:
      print('You win!!')
      break


