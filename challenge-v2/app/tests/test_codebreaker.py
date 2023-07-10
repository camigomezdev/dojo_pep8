""" Test file for CodeBreaker """
import unittest
import configparser

from app.models.codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """ Class for unittest CodeBreaker """

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
        self.assertEqual('XX X', codebreaker.challenge())

    def test_codebreaker_test_chars2(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '1059', 'Guest', False)
        self.assertEqual('XXX ', codebreaker.challenge())

    def test_codebreaker_test_chars3(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '9782', 'Guest', False)
        self.assertEqual('  _ ', codebreaker.challenge())

    def test_codebreaker_test_chars4(self):
        """
        Random number insertion test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '9504', 'Guest', False)
        self.assertEqual(' __ ', codebreaker.challenge())

    def test_codebreaker_fail_chars(self):
        """
        No repeated digits test
        """
        codebreaker = CodeBreaker(self.lang, self.cfg, '9999', 'Guest', False)
        test = None
        self.assertEqual(test, codebreaker.challenge())


if __name__ == '__main__':
    unittest.main()
