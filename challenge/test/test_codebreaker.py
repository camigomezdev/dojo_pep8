""" Test file for CodeBreaker """
import unittest

from codebreaker import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    """ Class for unittest CodeBreaker """

    def setUp(self):
        """
        Instance CodeBreaker()
        """
        self.codebreaker = CodeBreaker()

    def test_codebreaker_win(self):
        """
        Win Result Test
        """
        resolve = self.codebreaker.guess_number('1058')

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
        resolve = self.codebreaker.guess_number('1078')
        self.assertEqual('XX X', resolve)

    def test_codebreaker_test_chars2(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('1059')
        self.assertEqual('XXX ', resolve)

    def test_codebreaker_test_chars3(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('9782')
        self.assertEqual('  _ ', resolve)

    def test_codebreaker_test_chars4(self):
        """
        Random number insertion test
        """
        resolve = self.codebreaker.guess_number('9504')
        self.assertEqual(' __ ', resolve)

    def test_codebreaker_fail_chars(self):
        """
        No repeated digits test
        """
        resolve = self.codebreaker.guess_number('9999')
        test = 'Error: No repeated numbers allowed!'
        self.assertEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
