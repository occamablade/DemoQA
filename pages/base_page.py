"""A base page class"""
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """
    Class with base page methods
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        logger.info(f'Open {self.url}')
        return self.driver.get(self.url)
