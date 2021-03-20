import logging
import pytest



logging.basicConfig(filename='config_check.log', level=logging.INFO)
logging.info('start')
pytest.main()
logging.info('done')