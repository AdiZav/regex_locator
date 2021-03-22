import os
import datetime
import logging
import re
import pytest
from lorem_text import lorem
import random
import string
from ..main import Locator


"""
test_file_name_length.py runs tests directly on the Locator class.
It's goal is to test whether different file name length affect the accuracy of the classes' scan.
"""

TEST_FOLDER_PATH = 'tests/test_files/test_file_name_length'
EXP = r'b\w{2}'
NAME_CHARS = string.ascii_letters + string.digits


def create_test_file(file_info):
    """
    Creates random files to run the test on,
    and return the correct amount of matches.
    """

    txt = lorem.paragraphs(5)
    count = len(re.findall(EXP, txt))
    f = open('{}/{}'.format(TEST_FOLDER_PATH, file_info[0]), 'w')
    f.write(txt)
    f.close()
    return count


@pytest.fixture(params=[(''.join(random.choice(NAME_CHARS) for i in range(8)),),
                        (''.join(random.choice(NAME_CHARS) for i in range(20)),),
                        (''.join(random.choice(NAME_CHARS) for i in range(30)),)])
def file_info(request):
    return request.param


def test_amount(file_info):
    try:
        os.mkdir(TEST_FOLDER_PATH)
    except FileExistsError as e:
        pass

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_name_length.py')
    expected = create_test_file(file_info)
    locator = Locator(EXP, False, False, ['{}/{}'.format(TEST_FOLDER_PATH, file_info[0])])
    locator.analyze_files()
    output = locator.get_match_count()

    # Log an error if Locator() returns an incorrect amount of matches
    if expected != output:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_name_length.py\t'
                      f'expected - {expected} output - {output}')
    assert expected == output




