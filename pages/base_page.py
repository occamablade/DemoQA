"""A base page class"""

import logging

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from conf.conf import Timeouts

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
    def action_double_click(self, element):
        logger.info('Double Click')
        return ActionChains(self.driver).double_click(element).perform()

    @allure.step('Action right click')
    def action_right_click(self, element):
        logger.info('Right Click')
        return ActionChains(self.driver).context_click(element).perform()

    def element_is_present(self, locator, timeout=Timeouts.sec_5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator, timeout=Timeouts.sec_5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_is_clickable(self, locator, timeout=Timeouts.sec_5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def elements_are_present(self, locator, timeout=Timeouts.sec_5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
