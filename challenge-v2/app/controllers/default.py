""" Default Controller for CodeBreaker"""
import configparser

from app.models.codebreaker import CodeBreaker
from app.views.default import DefaultView


class DefaultController:
    """ Class for Default Controller """

    @classmethod
    def show_credits(cls, print_credits: True) -> str | dict:
        """
        Prints at exit the app all credits if print_credits is True,
        else returns a dictionary with credits (str/dict)
        """
        info = {
            'title': 'CodeBreaker',
            'version': '2.0.1',
            'date': '2023-05-25',
            'developer': 'Gonzalo Mahserdjian',
            'developer_alias': 'gsmx64',
            'package': 'Bootcamp Código Facilito Python Avanzado',
            'subpackage': 'Class 01 Practice Challenge',
            'class': 'Dojo PEP and good practices',
            'bootcamp roadmap': 'https://codigofacilito.com/bootcamps/python-avanzado/roadmap',  # noqa: E501  # pylint: disable=line-too-long
            'license': 'GNU/GPL version 3',
            'license link': 'https://www.gnu.org/licenses/gpl-3.0.txt'
        }

        if print_credits:
            for keys, values in info.items():
                print(f'{keys}: {values}')

        return info

    @classmethod
    def create_app(cls) -> None:
        """
        Inits this App
        """
        cls.cfg = configparser.ConfigParser()
        cls.cfg.sections()
        cls.cfg.read('app/config.ini', 'UTF-8')

        cls.lang = configparser.ConfigParser()
        cls.lang.sections()
        cls.lang.read('app/languages/'+cls.cfg["LANGUAGE"]
                      ["DEFAULT_LANGUAGE"]+'.ini', 'UTF-8')

        cls.tries = 1
        cls.total_tries = 10
        cls.view = DefaultView()

        cls.view.clean_screen()
        print(cls.view.get_intro())

        current_language_input = cls.view.input_language(cls.lang)
        current_language = cls.current_language(
            cls, current_language_input,
            cls.cfg["LANGUAGE"]["DEFAULT_LANGUAGE"])
        cls.lang.read('app/languages/'+current_language+'.ini', 'UTF-8')

        cls.view.input_start(cls.lang)
        cls.view.clean_screen()

        cls._go_to_menu(cls)
        print(cls.view.get_exit(cls.lang))

    def _go_to_menu(self) -> None:
        """
        Builds the first level menu options
        """
        print(self.view.get_intro())

        menus = {'1': self.lang["LANG"]["LANG_RUN_EASY_MODE"],
                 '2': self.lang["LANG"]["LANG_RUN_NORMAL_MODE"],
                 '3': self.lang["LANG"]["LANG_RUN_HARD_MODE"],
                 'Q': self.lang["LANG"]["LANG_QUIT_LEYEND"]}

        for index, value in menus.items():
            print(self.view.get_menu_options(index, value))

        print(self.view.get_linebrake(), end='')
        option = self.view.get_input(self.lang)

        if option in menus.keys() and option.lower() != 'q':  # noqa: E501  # pylint: disable=consider-iterating-dictionary
            self._go_to_option(self, option)  # noqa: E501  # pylint: disable=too-many-function-args

        elif option.lower() == 'q':
            print(self.view.get_exit(self.lang))
        else:
            self.view.clean_screen()
            self._go_to_menu(self)  # noqa: E501  # pylint: disable=too-many-function-args
            self.view.clean_screen()

    def _go_to_option(self, mode) -> None:
        """
        Builds the first level menu options
        """
        self.view.clean_screen()
        print(self.view.get_intro())
        print(self.view.get_text_formated(
            self.lang["LANG"]["LANG_INSERT_NAME"]))
        username = self.view.input_username(self.lang)

        print('[CodeBreaker] '+self.lang["LANG"]
              ["LANG_PLAYER_IS"].format(username))

        if mode == '1':  # Easy mode
            self.total_tries = self.cfg.getint("OPTIONS", "TOTAL_TRIES_EASY")  # noqa: E501  # pylint: disable=pointless-statement
            print(self.view.get_text_formated(
                self.lang["LANG"]["LANG_EASY_MODE"]))
            random_with_duplicates = False

        if mode == '2':  # Normal mode
            self.total_tries = self.cfg.getint("OPTIONS", "TOTAL_TRIES_NORMAL")  # noqa: E501  # pylint: disable=pointless-statement
            print(self.view.get_text_formated(
                self.lang["LANG"]["LANG_NORMAL_MODE"]))
            random_with_duplicates = False

        if mode == '3':  # Hard mode
            self.total_tries = self.cfg.getint("OPTIONS", "TOTAL_TRIES_HARD")  # noqa: E501  # pylint: disable=pointless-statement
            print(self.view.get_text_formated(
                self.lang["LANG"]["LANG_HARD_MODE"]))
            print(self.view.get_text_formated(
                self.lang["LANG"]["LANG_DUPLICATED_DIGITS_ENABLED"]))
            random_with_duplicates = True

        print(self.view.get_insert_number(self.lang, self.total_tries))
        number = self.view.input_number(self.lang)

        codebreaker = CodeBreaker(self.lang,
                                  self.cfg,
                                  number,
                                  username,
                                  random_with_duplicates)

        while self.tries != self.total_tries:

            challenge = codebreaker.challenge()

            if challenge:
                self.view.clean_screen()
                print(self.view.get_intro())

                print(self.view.get_text_formated(
                    self.lang["LANG"]["LANG_NUMBER_INSERTED"].format(number)))
                print(self.view.get_text_formated(
                    self.lang["LANG"]["LANG_OUTPUT_RESULT"].format(challenge)))
                self.tries += 1
                tries_remain = self.total_tries-self.tries+1

                # print(f'TESTING!!! - REAL NUMBER: {codebreaker.realnumber}')
                print(self.view.get_tries_remain(self.lang, tries_remain))

            codebreaker.update_number(self.view.input_number(self.lang))

            if isinstance(codebreaker.is_winner,
                          bool) and codebreaker.is_winner:
                print(self.view.get_winner(self.lang, codebreaker.realnumber))
                self.view.input_pause(self.lang)
                break

        else:  # noqa: E501
            print(self.view.get_game_over(self.lang,
                                          codebreaker.realnumber))
            self.view.input_pause(self.lang)

        self.tries = 1
        self.view.clean_screen()
        self._go_to_menu(self)  # pylint: disable=E1121

    def current_language(self, current_language_input: str,
                         default_language='en') -> str:
        """
        Gets from first input the current short tag for
        language or default language from config (str)
        """
        if current_language_input == '1':
            current_language = 'en'
        elif current_language_input == '2':
            current_language = 'es'
        else:
            current_language = default_language
        return current_language
