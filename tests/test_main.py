"""
A module for test main in the tests package.
"""
import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from codebreaker import Codebreaker
from main import play_codebreaker


def test_play_codebreaker(
        monkeypatch: MonkeyPatch, captured_print: CaptureFixture
) -> None:
    """
    Test play_codebreaker function from main module.
    The function should handle user input and provide feedback.
    :param monkeypatch: pytest's built-in fixture for mocking
    :type monkeypatch: _pytest.monkeypatch.MonkeyPatch
    :param captured_print: pytest's built-in fixture to capture print
     statements
    :type captured_print: _pytest.capture.CaptureFixture
    :return: None
    :rtype: NoneType
    """
    inputs = ['1234', '2345', '3456', 'abc', '1111']
    outputs = ['X___', 'XX__', 'XXX_', ValueError(
        'Invalid guess. Must be a 4-digit number with unique digits.'
    ), ValueError(
        'Invalid guess. Must be a 4-digit number with unique digits.')]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    monkeypatch.setattr(
        Codebreaker, 'guess', lambda self, guess: outputs.pop(0))

    with pytest.raises(IndexError):
        play_codebreaker()

    captured = captured_print.readouterr()
    assert "Let's play Codebreaker!\nYou have 10 attempts." in captured.out
    assert 'X___' in captured.out
    assert 'XX__' in captured.out
    assert 'XXX_' in captured.out
    assert 'Invalid guess. Must be a 4-digit number with unique digits.' in\
           captured.out
    assert 'You have reached the maximum number of tries. You lost.' not in\
           captured.out
