# numerical sequence to guess
TRUE_NUMBER = "4263"


class Codebreaker:

    # method to guess the number, number is entered by the user
    def guess_number(self, number=None):

        # if there is no numerical sequence
        if TRUE_NUMBER == '':
            return 'Number is not defined'

        # if the number entered by the user is not 4 digits
        if number is None or len(str(number)) != 4:
            return "Error. Enter a number of 4 digits"

        # if the number entered by the user is equal to the numerical sequence
        if str(number) == TRUE_NUMBER:
            return True

        # string to be returned to the user as feedback
        feedback_to_user = ''

        # convert number to list
        number = [int(digit) for digit in str(number)]

        # iterate around the list of digits and compare
        for index, digit in enumerate(number):
            # compare if the digits are equals and in the same position
            if TRUE_NUMBER[index] == str(number[index]):
                feedback_to_user += 'X'

            # compare if the digits are equals but in different position
            elif str(digit) in TRUE_NUMBER:
                feedback_to_user += '_'

            # if the digit is not in the numerical sequence
            else:
                feedback_to_user += " "

        # print the feedback_to_user
        print(feedback_to_user)

        return False


# main method
if __name__ == "__main__":
    # while the user not enter a number of 4 digits or not win the game
    while True:
        try:
            user_number = int(input("Please enter a number: "))
            feedback_to_user = Codebreaker().guess_number(user_number)
            if feedback_to_user:
                print("Congratulations, you are the win!")
                break
        except ValueError:
            print("Oops! That was no valid number. Try again.")
