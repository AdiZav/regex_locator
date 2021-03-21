#! /usr/bin/python

import os
import datetime
import logging
import re
import pytest
from lorem_text import lorem
from ..main import Locator


"""
test_file_size.py runs tests directly on the Locator class.
It's goal is to test whether different file sizes affect the accuracy of the classes' scan.
"""

TEST_FOLDER_PATH = 'tests/test_files/test_file_size'
EXP = r'b\w{2}'


def create_test_file(file_info):
    """
    Creates random files to run the test on,
    and return the correct amount of matches.
    """

    txt = lorem.paragraphs(file_info[1])  # Generates random strings.
    count = len(re.findall(EXP, txt))
    f = open('{}/{}'.format(TEST_FOLDER_PATH, file_info[0]), 'w')
    f.write(txt)
    f.close()
    return count

# Each tuple represents the file to be created for the test - ('file_name', 'file_size')
@pytest.fixture(params=[('small.txt', 10), ('medium.txt', 100), ('large.txt', 1000)])
def file_info(request):
    return request.param


def test_amount(file_info):
    try:
        os.mkdir(TEST_FOLDER_PATH)  # Create folder for random files
    except FileExistsError as e:
        pass

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_size.py')
    expected = create_test_file(file_info)
    locator = Locator(EXP, False, False, ['{}/{}'.format(TEST_FOLDER_PATH, file_info[0])])
    locator.analyze_files()
    output = locator.get_match_count()

    # Log an error if Locator() returns an incorrect amount of matches
    if expected != output:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_size.py\t'
                      f'expected - {expected} output - {output}')
    assert expected == output




