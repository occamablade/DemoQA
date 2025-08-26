"""Module with fixtures"""

import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from conf.conf import Timeouts

logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    """
    Fixture start driver session
    :return: driver
    """
    logger.warning('Start new session driver')
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Timeouts.sec_5)
    driver.maximize_window()
    yield driver
    logger.warning('End session driver')
    driver.quit()
