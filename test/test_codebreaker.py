""" Test file for CodeBreaker"""
# __doc__ (Test file for little game CodeBreaker where you must guess
# the secret number)

import unittest

from codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """
    Class for unittest CodeBreaker
    """

    def setUp(self):
        """
        Instance CodeBreaker()
        """
        self.codebreaker = CodeBreaker()

    def test_codebreaker_win(self):
        """
        Win Result Test
        """
        resolve = self.codebreaker.guess_number('1010')

        self.assertTrue(resolve)

    def test_codebreaker_fail_input(self):
        """
        Fail input characters
        """
        resolve = self.codebreaker.guess_number('12345')
        self.assertEqual('Error: Insert only 4 numbers!', resolve)

    def test_codebreaker_test_chars1(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('1020')
        self.assertEqual('XX?X', resolve)

    def test_codebreaker_test_chars2(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('1011')
        self.assertEqual('XXX_', resolve)

    def test_codebreaker_test_chars3(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('9909')
        self.assertEqual('??_?', resolve)

    def test_codebreaker_fail_chars(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('9999')
        self.assertEqual('????', resolve)


if __name__ == '__main__':
    unittest.main()
