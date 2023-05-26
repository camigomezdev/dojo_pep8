"""
A module for test codebreaker in the tests package.
"""
import pytest

from codebreaker import Codebreaker


def test_generate_random_number() -> None:
    """
    Test _generate_random_number function from Codebreaker class.
    The function should return a 4-digit number with unique digits.
    :return: None
    :rtype: NoneType
    """
    codebreaker: Codebreaker = Codebreaker()
    number: str = codebreaker._generate_random_number()
    assert len(number) == 4
    assert number.isdecimal()
    assert len(set(number)) == 4


def test_generate_feedback() -> None:
    """
    Test _generate_feedback function from Codebreaker class.
    The function should return a string containing "X" for each correct
     digit at the right position and "_" for each correct digit at the
     wrong position.
    :return: None
    :rtype: NoneType
    """
    codebreaker: Codebreaker = Codebreaker()
    codebreaker.right_number = "1234"

    assert codebreaker._generate_feedback("1234") == "XXXX"
    assert codebreaker._generate_feedback("4321") == "____"
    assert codebreaker._generate_feedback("1256") == "XX"
    assert codebreaker._generate_feedback("5678") == ""


def test_guess() -> None:
    """
    Test guess function from Codebreaker class.
    The function should return "XXXX" if the guess is correct;
     otherwise, feedback on the guess.
    :return: None
    :rtype: NoneType
    """
    codebreaker: Codebreaker = Codebreaker()
    codebreaker.right_number = "1234"

    assert codebreaker.guess("1234") == "XXXX"
    assert codebreaker.guess("4321") == "____"
    assert codebreaker.guess("1256") == "XX"
    assert codebreaker.guess("5678") == ""

    with pytest.raises(ValueError):
        codebreaker.guess("1")
        codebreaker.guess("12345")
        codebreaker.guess("abcd")
        codebreaker.guess("1122")
