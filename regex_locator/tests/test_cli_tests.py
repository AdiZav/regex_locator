import pytest
import logging
import datetime

from .. import regex_locator


def test_normal(capsys):
    """Make sure no error is thrown on valid input"""

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_normal')
    regex_locator.main(**{'regex': "r'b\w{2}'", 'files': ["./tests/test_files/basic.txt"],
                          'color': "blue", 'machine': True})
    out, err = capsys.readouterr()

    if err != '':
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_normal')
    assert err == ''


def test_missing_exp():
    """Make sure an error is thrown when not passing a regex"""

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_missing_exp')

    raised = False
    with pytest.raises(Exception):
        regex_locator.main(**{'files': ["./tests/test_files/basic.txt"],
                              'color': "blue", 'machine': True})
        raised = True

    if not raised:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_missing_exp')


def test_optional_args(capsys):
    """Make sure no error is thrown when optional arguments aren't passed"""

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_optional_args')
    regex_locator.main(**{'regex': "r'b\w{2}'", 'files': ["./tests/test_files/basic.txt"],
                          'color': None, 'machine': False})
    out, err = capsys.readouterr()

    if err != '':
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_optional_args')
    assert err == ''


def test_missing_file():
    """Make sure an error is thrown when passing a nonexistent file"""

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_missing_file')

    raised = False
    with pytest.raises(Exception):
        regex_locator.main(**{'regex': "r'b\w{2}'", 'files': ["./tests/test_files/basic1.txt"],
                              'color': "blue", 'machine': True})
        raised = True

    if not raised:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_missing_file')


def test_no_file():
    """Make sure an error is thrown when no file is passed"""

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_no_file')

    raised = False
    with pytest.raises(Exception):
        regex_locator.main(**{'regex': "r'b\w{2}'",
                              'color': "blue", 'machine': True})
        raised = True

    if not raised:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_no_file')





