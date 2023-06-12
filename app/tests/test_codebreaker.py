""" Test file for CodeBreaker"""
# __doc__ (Test file for little game CodeBreaker)

import unittest
import configparser

from app.models.codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """
    Class for unittest CodeBreaker
    """

    def setUp(self):
        """
        Instance CodeBreaker()
        """
        self.cfg = configparser.ConfigParser()
        self.cfg.sections()
        self.cfg.read('app/tests/config_tests.ini', 'UTF-8')

        self.lang = configparser.ConfigParser()
        self.lang.sections()
        self.lang.read('app/languages/'+self.cfg["LANGUAGE"]
                       ["DEFAULT_LANGUAGE"]+'.ini', 'UTF-8')

    def test_codebreaker_win(self):
        """
        Win Result Test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '1058', 'Guest', False)
        self.assertTrue(codebreaker)

    def test_codebreaker_test_chars1(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '1078', 'Guest', False)
        self.assertEqual('XX?X', codebreaker.challenge())

    def test_codebreaker_test_chars2(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '1051', 'Guest', False)
        self.assertEqual('XXX_', codebreaker.challenge())

    def test_codebreaker_test_chars3(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '9782', 'Guest', False)
        self.assertEqual('??_?', codebreaker.challenge())

    def test_codebreaker_fail_chars(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '9999', 'Guest', False)
        self.assertEqual('????', codebreaker.challenge())


if __name__ == '__main__':
    unittest.main()
