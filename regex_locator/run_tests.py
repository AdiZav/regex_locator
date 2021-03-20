#! /usr/bin/python

import logging
import pytest



logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('start')
pytest.main()
logging.info('done')