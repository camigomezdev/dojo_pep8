"""
A module for test logging config in the tests.test_core package.
"""
import logging
import os
from datetime import datetime
from pathlib import Path

from core.logging_config import (
    _build_log_filename,
    _configure_file_handler,
    _create_logs_folder,
)


def test_create_logs_folder() -> None:
    """
    Test _create_logs_folder function from logging_config.
    The function should create a logs folder and return its path.
    :return: None
    :rtype: NoneType
    """
    logs_folder_path: str = _create_logs_folder()
    assert os.path.exists(logs_folder_path)
    assert os.path.basename(logs_folder_path) == 'logs'


def test_build_log_filename() -> None:
    """
    Test _build_log_filename function from logging_config.
    The function should return a log filename in the format
     log-{current_date}.log.
    :return: None
    :rtype: NoneType
    """
    log_filename: str = _build_log_filename()
    current_date = datetime.today().strftime('%d-%b-%Y-%H-%M-%S')
    assert log_filename == f"log-{current_date}.log"


def test_configure_file_handler(tmp_path: Path) -> None:
    """
    Test _configure_file_handler function from logging_config.
    The function should return a logging.FileHandler instance with the
     provided filename and log level.
    :param tmp_path: The Temporary directory
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    log_filename: str = str(tmp_path / 'test.log')
    log_level: int = logging.DEBUG
    file_handler: logging.FileHandler = _configure_file_handler(
        log_filename, log_level)
    fmt: str = "[%(name)s][%(asctime)s][%(levelname)s][%(module)s]" \
               "[%(funcName)s][%(lineno)d]: %(message)s"
    assert isinstance(file_handler, logging.FileHandler)
    assert file_handler.level == log_level
    assert isinstance(file_handler.formatter, logging.Formatter)
    assert file_handler.formatter._fmt == fmt
