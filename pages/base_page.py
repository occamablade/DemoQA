"""A base page class"""

from conf.conf import Timeouts

class BasePage:
    """
    Class with base page methods
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(Timeouts.sec_5)

    def get_url(self):
        get_url = self.driver.current_url
        return get_url

    def open(self):
        return self.driver.get(self.url)
