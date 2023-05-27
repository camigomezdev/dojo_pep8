from codebreaker import Codebreaker


TOTAL_ATTEMPS = 10

codebreaker = Codebreaker()

attemps = 0

print("Let's play Codebreaker!!")

while attemps != TOTAL_ATTEMPS:
    attemps += 1

    number = input("Number: ")
    try:
        resolve = codebreaker.guess(number)
        if isinstance(resolve, bool):
            print("You win!!")
            print(f"You needed just {attemps} to guess :)")
            break
        else:
            if resolve:
                print(f"Nice try: {resolve}")
            print("Please keep guessing...")
    except Exception as err:
        print(f"error: {str(err)}")
