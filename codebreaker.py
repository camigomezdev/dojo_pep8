"""Here we import the module random because we generate a random number"""
import random


class CodeBreaker:
    """Return a result to the comparation between random number and user number"""

    def __init__(self) -> None:
        """In this section we generate a random number with 4 digits."""
        list_numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        self.true_number = random.sample(list_numbers, 4)
        self.true_number = "".join(self.true_number)

    def adivinar(self, user_number=None):
        """This function helps us to compare the random number with the user number 
        and define if they are the same """
        if self.true_number == '':
            return 'Number is not defined'

        if user_number is None or len(user_number) != 4 or 'e' in list(user_number):
            return "Error, please enter a correct number according to the given convention"

        if user_number == self.true_number:
            return 1

        array_n = ""
        user_number_list = list(user_number)
        validate_duplicate_digits = []
        for number_d in user_number_list:
            if number_d in validate_duplicate_digits:
                return "Error, you cannot have duplicate numbers in your sequence"
            validate_duplicate_digits.append(number_d)

        for i, number in enumerate(user_number_list):
            if self.true_number[i] == number:
                array_n += 'X'

            elif number in self.true_number:
                array_n += '_'

            else:
                array_n += 'E'

        return array_n
