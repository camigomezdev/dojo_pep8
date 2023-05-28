"""
Test for Code Breaker game
"""
import unittest

from code_breaker import BadFormat
from code_breaker import BadLength
from code_breaker import BadType
from code_breaker import CodeBreaker
from code_breaker import InvalidTrueNumber
from code_breaker import RepeatedDigit


class TestCodeBreaker(unittest.TestCase):
    """
    Test Suit for Code Breaker game
    """

    def setUp(self):
        self.__code_breaker = CodeBreaker("1234")

    def test_bad_secret(self):
        with self.assertRaises(InvalidTrueNumber):
            CodeBreaker("")

    def test_none_type(self):
        with self.assertRaises(BadType):
            self.__code_breaker.guess()

    def test_bad_type(self):
        with self.assertRaises(BadType):
            self.__code_breaker.guess(1234)

    def test_bad_length(self):
        with self.assertRaises(BadLength):
            self.__code_breaker.guess("123")

    def test_no_digit(self):
        with self.assertRaises(BadFormat):
            self.__code_breaker.guess("foo1")

    def test_repeat_digit(self):
        with self.assertRaises(RepeatedDigit):
            self.__code_breaker.guess("1212")

    def test_correct_number(self):
        number = "1234"
        expected_result = True
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_correct_bad_positioned_incorrect_number(self):
        number = "1356"
        expected_result = "X_##"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_correct_incorrect_number(self):
        number = "1536"
        expected_result = "X#X#"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_correct_bad_positioned_number(self):
        number = "1432"
        expected_result = "X_X_"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_incorrect_bad_positioned_number(self):
        number = "5362"
        expected_result = "#_#_"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_incorrect_number(self):
        number = "5678"
        expected_result = "####"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)

    def test_bad_positioned_number(self):
        number = "4321"
        expected_result = "____"
        result = self.__code_breaker.guess(number)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
