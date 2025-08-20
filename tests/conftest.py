from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from conf.conf import Timeouts


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Timeouts.sec_5)
    driver.maximize_window()
    yield driver
    driver.quit()