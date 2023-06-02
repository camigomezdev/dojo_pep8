from helpers import is_number, is_numerical_sequence

TRUE_NUMBER = "4567"
RETRY_MESSAGE = "Please Retry Again!"
ATTEMPS_LIMIT = 10


class Codebreaker:
    """The goal is to guess a 4 digit number."""

    def __init__(self):
        print("Lets go to play code breaker!!")

    def validate_number_conditions(self, number: str) -> tuple[bool, str]:
        """This function check the validate the conditions to accept the number
        And start to play
        """
        if not is_number(number):
            return False, f"It isn't a number!{RETRY_MESSAGE}"

        if not number or number is None:
            return False, f"Number doesn't exist!{RETRY_MESSAGE}"

        if len(number) != 4:
            return (
                False,
                f"Number doesn't met the requirements! \
                       {RETRY_MESSAGE}",
            )

        if not is_numerical_sequence(list(number)):
            return (
                False,
                f"The number isn't a numerical sequence! \
                    {RETRY_MESSAGE}",
            )

        return True, "The number meets the requirements!"

    def check_sequence_number(self, number: str) -> str:
        resultado = ""

        for i in range(len(number)):
            if number[i] == TRUE_NUMBER[i]:
                resultado += "X"
            elif number[i] in TRUE_NUMBER:
                resultado += "_"
            else:
                resultado += " "
        return resultado

    def guess_number(self, number: str) -> tuple[bool, str]:
        """This function play the game and gess the number"""

        if number == TRUE_NUMBER:
            return True, "XXXX"

        return False, self.check_sequence_number(number)

    def play(self) -> tuple[bool, str]:
        attemps = 1
        while True:
            number = input("Code Breaker, Enter the sequence number:")
            validate_number = self.validate_number_conditions(number)
            if validate_number[0]:
                result = self.guess_number(number)
                if result[0]:
                    print(
                        f"{result[1]}. Congratulations you win in "
                        f"{attemps} attempts!!!"
                    )
                    break
                else:
                    print(f"{result[1]}.{RETRY_MESSAGE} Attemps:{attemps}")
            elif attemps != ATTEMPS_LIMIT:
                result = validate_number
                print(f"{result[1]}.{RETRY_MESSAGE} Attemps:{attemps}")
            else:
                print(
                    f"{result[1]}. You lose! :(. You Exceed your "
                    f"{attemps} attempts!!!"
                )
                break
            attemps += 1
