"""A base page class"""
import logging

import allure
from selenium.webdriver import ActionChains

logger = logging.getLogger(__name__)

class BasePage:
    """
    Class with base page methods
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open new url')
    def open(self):
        logger.info(f'Open {self.url}')
        return self.driver.get(self.url)

    @allure.step('Action double click')
    def mouse_double_click(self, element):
        logger.info('Double Click')
        return ActionChains(self.driver).double_click(element).perform()

    @allure.step('Action right click')
    def mouse_right_click(self, element):
        logger.info('Right Click')
        return ActionChains(self.driver).context_click(element).perform()

    @allure.step('Action one click')
    def mouse_click(self, element):
        logger.info('Click')
        return ActionChains(self.driver).click(element).perform()