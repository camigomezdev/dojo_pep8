""" Default View for CodeBreaker """
import os

from app.decorators.decorators_views import decorate_intro


class DefaultView:
    """ Class for Default View """

    @decorate_intro(num_lines=3)  # pylint: disable=redundant-keyword-arg
    def get_intro(self) -> str:
        """
        Prints App intro message
        """
        return '                 CodeBreaker!  \n'

    @decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_exit(self, lang: object) -> str:
        """
        Prints App exit message
        """
        self.clean_screen()
        return f' >>> {lang["LANG"]["LANG_EXIT_PROGRAM"]} \n'

    def get_menu_options(self, key: str, value: str) -> str:
        """
        Format the Menu Options
        """
        return f'[{key}] {value} '

    def get_input(self, lang: object) -> str:
        """
        Returns the select option input
        """
        return input(f'{lang["LANG"]["LANG_INPUT_SELECT_OPTION"]} ')

    @decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_winner(self, lang: object, number: str) -> str:
        """
        Prints App exit message
        """
        message = f'                 {lang["LANG"]["LANG_YOU_WIN_TITLE"]} \n'
        message += '-'*49+' \n'
        message += lang["LANG"]["LANG_YOU_WIN_DESC"].format(number) + ' \n'
        return message

    @decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_game_over(self, lang: object, number: str) -> str:
        """
        Prints App exit message
        """
        message = f'                 {lang["LANG"]["LANG_GAME_OVER_TITLE"]} \n'
        message += '-'*49+' \n'
        message += lang["LANG"]["LANG_GAME_OVER_DESC"].format(number) + ' \n'
        return message

    def get_tries_remain(self, lang: object, value: str) -> str:
        """
        Returns tries remain
        """
        message = '[CodeBreaker] ' + \
            lang["LANG"]["LANG_TRIES_REMAIN"].format(value)
        return message

    def get_text_formated(self, text: str) -> str:
        """
        Returns the player`s name
        """
        message = f'[CodeBreaker] {text}'
        return message

    def get_insert_number(self, lang: object, total_tries: str) -> str:
        """
        Returns the inserted number
        """
        message = '[CodeBreaker] ' + \
            lang["LANG"]["LANG_ONLY_FOUR_NUMBERS"].format(total_tries)
        return message

    def input_username(self, lang: object) -> str:
        """
        Returns the insert player`s name input
        """
        return input(f'[CodeBreaker] {lang["LANG"]["LANG_INPUT_PLAYER"]}: ') or lang["LANG"]["LANG_ANONIMOUS_PLAYER"]  # noqa: E501  # pylint: disable=line-too-long

    def input_number(self, lang: object) -> str:
        """
        Returns the tried number input
        """
        return input(f'[CodeBreaker] {lang["LANG"]["LANG_INPUT_NUMBER"]}: ')

    def get_linebrake(self) -> str:
        """
        Format the Menu Options
        """
        return '\n'

    def input_language(self, lang: object) -> str:
        """
        Returns the select option input
        """
        return input(f'{lang["LANG"]["LANG_SELECT_LANGUAGE"]} ')

    def input_start(self, lang: object) -> str:
        """
        Returns the select option input
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_START"]}')

    def input_pause(self, lang: object) -> str:
        """
        Returns the intro press a key pause
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_CONTINUE"]} ')

    def clean_screen(self) -> None:
        """
        Makes a clear screen in view, cls for Windows,
        clear for Unix/Linux
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
