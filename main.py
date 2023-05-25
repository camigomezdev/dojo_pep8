from codebreaker import Codebreaker


TOTAL_ATTEMPS = 10

codebreaker = Codebreaker()

attemp = 0

print("Let's play Codebreaker!!")

while attemp != TOTAL_ATTEMPS:
    number = input("Number:")
    resolve = codebreaker.guess(number)
    print(resolve)

    if resolve:
        print("You win!!")
        break
