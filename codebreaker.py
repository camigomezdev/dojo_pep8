import random
from typing import Union


class Codebreaker:
    def __init__(self) -> None:
        self.NUMBER_TO_GUESS = "".join(random.sample("0123456789", 4))
        print(f"number to guess 👀: {self.NUMBER_TO_GUESS}")

    def guess(self, number: str = None) -> Union[bool, str]:
        if not self.NUMBER_TO_GUESS:
            raise Exception("Number is not defined")
        elif not number.isdecimal():
            raise Exception("Number must be decimal")
        elif len(number) != 4:
            raise Exception("Number must have 4 digits")
        elif number == self.NUMBER_TO_GUESS:
            return True

        array_number = []
        for _, digit in enumerate(number):
            if digit in array_number:
                raise Exception("Number must not have repeated digits")
            array_number.append(digit)

        result_x = ""
        result__ = ""
        number = list(number)
        for index, digit in enumerate(number):
            if self.NUMBER_TO_GUESS[index] == number[index]:
                result_x += "X"
            elif digit in self.NUMBER_TO_GUESS:
                result__ += "_"

        return result_x + result__
