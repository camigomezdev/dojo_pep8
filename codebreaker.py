"""
Module wiht the Codebreaker Class
"""

import random

class CodeBreaker:
    def __init__(self) -> None:
        self.hidden_number = ''

    def get_random_num(self):
        return ''.join(random.sample("123456789", 4))
    
    def set_hidden_number(self, hidden_number=None):
        """
        This function assings the hidden number to the parameter self
        in case hidden number values none generates a new hidden 
        number 
        """
        if hidden_number is None:
            hidden_number = self.get_random_num()
        
        try:
            self.is_valid_len_number(hidden_number)
            self.is_a_number(hidden_number)
            self.does_not_contain_repeated_digits(hidden_number)

        except Exception as e:
            raise e
        
        self.hidden_number = hidden_number

    def play(self):
        attempt = 1

        print('Lets play Code Breaker!')
        print('Try to guess the hidden number')

        while True:
            print(f'guess number {attempt}: ')
            number = input('')
            answer = self.guess_number(number)
            print(f'Answer: {answer}')

            if answer == 'XXXX':
                print(f'Congratulations! You have won in {attempt} attempts')
                return attempt
            
            attempt += 1
                  
    def guess_number(self, number=None):
        guess_position = ''
        guess_digit = ''

        for(index, digit) in enumerate(number):
            if digit == self.hidden_number[index]:
                guess_position += 'X'
            elif digit in self.hidden_number:
                guess_digit += ''

        return guess_position + guess_digit
    
    def is_valid_len_number(self, number):
        if len(number) != 4:
            raise Exception('This is not a valid length number')
        
        return True
    
    def is_a_number(self, number):
        if not number.isdecimal():
            raise Exception('You must type a 4 digit number')
        
        return True
    
    def does_not_contain_repeated_digits(self,number):
        for digit in number:
            if number.count(digit) > 1:
                raise Exception("It can't contain repeated digits")
            
        return True
    