import os
from codebreaker import CodeBreaker


def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For macOS and Linux
    else:
        _ = os.system('clear')


if __name__ == '__main__':
    codebreaker = CodeBreaker()
    action = input('Do you wanna play? (1) Play, (2) Exit: ')

    while action == '1':
        print('Player 1')
        hidden_number = input('Type the hidden number: ')
        codebreaker.set_hidden_number(hidden_number)
        clean()
        print('Player 2')
        attempt_player_2 = codebreaker.play()

        print('--------------------')
        print('Player 2')
        hidden_number = input('Escriba el número oculto: ')
        codebreaker.set_hidden_number(hidden_number)
        clean()
        print('Player 1')
        attempt_player_1 = codebreaker.play()

        print('--------------------')
        if attempt_player_1 > attempt_player_2:
            print('Player 1 wins')
        elif attempt_player_1 < attempt_player_2:
            print('Player 2 wins')
        else:
            print('It\'s a TIE!')
        
        print('--------------------')
        action = input('Continue? (1) Continue, (2) Exit: ')