""" Default View for CodeBreaker"""
# __doc__ (Default View file for little game CodeBreaker)

import os
import functools


class DefaultView:
    """
    Class for Default View

    Arguments:
    None

    Gets the view for this App.

    >>> view = DefaultView()
    True

    TODO:
        -

    """

    def _decorate_intro(num_lines: int) -> str:  # noqa: E501  # pylint: disable=no-self-argument
        """
        Decorator for intro and exit from app

        Arguments:
        num_lines (int)

        Repeat lines before and after of each intro or exit message (str)

        TODO:
            -
        """

        def decorator_decorate_intro(func: str):

            @functools.wraps(func)
            def wrapped_decorate_intro(self, *args, **kwargs) -> list:
                line = '-'*49+' \n'
                message = ''
                counter_start = counter_end = 1
                while counter_start <= num_lines:
                    message += line
                    counter_start += 1

                message += func(self, *args, **kwargs)

                while counter_end <= num_lines:
                    message += line
                    counter_end += 1

                return message
            return wrapped_decorate_intro
        return decorator_decorate_intro

    @_decorate_intro(num_lines=3)  # pylint: disable=redundant-keyword-arg
    def get_intro(self) -> str:
        """
        Function to get intro view message

        Arguments:
        self

        Prints App intro message (str)

        TODO:
            -
        """
        return '                 CodeBreaker!  \n'

    @_decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_exit(self, lang: object) -> str:
        """
        Function to get exit view message

        Arguments:
        lang (object)

        Prints App exit message (str)

        TODO:
            -
        """
        self.clean_screen()
        return f' >>> {lang["LANG"]["LANG_EXIT_PROGRAM"]} \n'

    def get_menu_options(self, key: str, value: str) -> str:
        """
        Function to get menu options view format

        Arguments:
        key (str)
        value (str)

        Format the Menu Options (str)

        TODO:
            -
        """
        return f'[{key}] {value} '

    def get_input(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_SELECT_OPTION"]} ')

    @_decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_winner(self, lang: object, number: str) -> str:
        """
        Function to get winner view message

        Arguments:
        lang (object)

        Prints App exit message (str)

        TODO:
            -
        """
        message = f'                 {lang["LANG"]["LANG_YOU_WIN_TITLE"]} \n'
        message += '-'*49+' \n'
        message += lang["LANG"]["LANG_YOU_WIN_DESC"].format(number) + ' \n'
        return message

    @_decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_game_over(self, lang: object, number: str) -> str:
        """
        Function to get game over view message

        Arguments:
        lang (object)
        number (str)

        Prints App exit message (str)

        TODO:
            -
        """
        message = f'                 {lang["LANG"]["LANG_GAME_OVER_TITLE"]} \n'
        message += '-'*49+' \n'
        message += lang["LANG"]["LANG_GAME_OVER_DESC"].format(number) + ' \n'
        return message

    def get_tries_remain(self, lang: object, value: str) -> str:
        """
        Function to format tries remain

        Arguments:
        self
        lang (object)

        Returns tries remain (str)

        TODO:
            -
        """
        message = '[CodeBreaker] ' + \
            lang["LANG"]["LANG_TRIES_REMAIN"].format(value)
        return message

    def get_text_formated(self, text: str) -> str:
        """
        Function to format player`s name

        Arguments:
        self
        lang (object)

        Returns the player`s name (str)

        TODO:
            -
        """
        message = f'[CodeBreaker] {text}'
        return message

    def get_insert_number(self, lang: object, total_tries: str) -> str:
        """
        Function to format the number

        Arguments:
        self
        lang (object)

        Returns the inserted number (str)

        TODO:
            -
        """
        message = '[CodeBreaker] ' + \
            lang["LANG"]["LANG_ONLY_FOUR_NUMBERS"].format(total_tries)
        return message

    def input_username(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the insert player`s name input (str)

        TODO:
            -
        """
        return input(f'[CodeBreaker] {lang["LANG"]["LANG_INPUT_PLAYER"]}: ') or lang["LANG"]["LANG_ANONIMOUS_PLAYER"]  # noqa: E501  # pylint: disable=line-too-long

    def input_number(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the tried number input (str)

        TODO:
            -
        """
        return input(f'[CodeBreaker] {lang["LANG"]["LANG_INPUT_NUMBER"]}: ')

    def get_linebrake(self) -> str:
        """
        Function to get a linebrake in view

        Arguments:
        self

        Format the Menu Options (str)

        TODO:
            -
        """
        return '\n'

    def input_language(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_SELECT_LANGUAGE"]} ')

    def input_start(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_START"]}')

    def input_pause(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the intro press a key pause (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_CONTINUE"]} ')

    def clean_screen(self) -> object:
        """
        Function to make a screen clear in view

        Arguments:
        self

        Make a screen clear in view, cls for Windows, clear for
        Unix/Linux (object)

        TODO:
            -
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
