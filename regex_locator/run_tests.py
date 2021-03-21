#! /usr/bin/python

import logging
import pytest

"""
Runs tests and logs them to - test.log
"""
logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('start')
pytest.main()
logging.info('done')