#! /usr/bin/python

import os
import re
import logging
import datetime
import pytest
from lorem_text import lorem
from ..main import Locator

"""
test_file_amount.py runs tests directly on the Locator class.
It's goal is to test whether the amount of files passed to the class affect the accuracy of the classes' scan.
"""

TEST_FOLDER_PATH = './tests/test_files/test_file_amount'
EXP = r'b\w{2}'


def create_test_files(test_info):
    """
    Creates random files to run the test on,
    and return the correct amount of matches.
    """

    match_count = 0
    for counter in range(test_info[1]):
        txt = lorem.paragraphs(5)
        match_count += len(re.findall(EXP, txt))
        f = open('{}/{}'.format(TEST_FOLDER_PATH, test_info[0]+'_'+str(counter+1)), 'w')
        f.write(txt)
        f.close()
    return match_count


# Each tuple represents the files to be created for the test - ('file_names', 'amount of files')
@pytest.fixture(params=[('first_test', 10), ('second_test', 15), ('third_test', 20)])
def test_info(request):
    return request.param


def test_amount(test_info):
    """Test whether Locator class can handle different amounts of files passed"""

    try:
        os.mkdir(TEST_FOLDER_PATH)
    except FileExistsError:
        pass

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_amount.py')
    expected = create_test_files(test_info)
    files = ['{}/{}_{}'.format(TEST_FOLDER_PATH, test_info[0], str(i+1)) for i in range(test_info[1])]
    locator = Locator(EXP, False, False, files)
    locator.analyze_files()
    output = locator.get_match_count()

    # Log an error if Locator() returns an incorrect amount of matches
    if expected != output:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_amount.py\t'
                      f'expected - {expected} output - {output}')
    assert expected == output