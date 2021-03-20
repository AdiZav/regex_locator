import pytest
from lorem_text import lorem
import re
import logging
import datetime
from ..regex_locator import Locator
import os

TEST_FOLDER_PATH = 'tests/test_files/test_file_size'
EXP = r'b\w{2}'


def create_test_file(file_info):
    txt = lorem.paragraphs(file_info[1])
    count = len(re.findall(EXP, txt))
    f = open('{}/{}'.format(TEST_FOLDER_PATH, file_info[0]), 'w')
    f.write(txt)
    f.close()
    return count


@pytest.fixture(params=[('small.txt', 10), ('medium.txt', 100), ('large.txt', 1000)])
def file_info(request):
    return request.param

def test_amount(file_info):
    try:
        os.mkdir(TEST_FOLDER_PATH)
    except FileExistsError as e:
        pass

    logging.info(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_size.py')
    expected = create_test_file(file_info)
    locator = Locator(EXP, False, False, ['{}/{}'.format(TEST_FOLDER_PATH, file_info[0])])
    locator.analyze_files()
    output = locator.get_match_count()

    if expected != output:
        logging.error(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} test_file_size.py\t'
                      f'expected - {expected} output - {output}')
    assert expected == output




