"""Module with method for links page"""

import logging
from typing import Any

import allure
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import LinkLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class LinkPage(BasePage):
    """A class with methods for links page"""

    def get_created_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.CREATED)

    def get_bad_request_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.BAD_REQUEST)

    def get_no_content_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.NO_CONTENT)

    def get_moved_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.MOVED)

    def get_unauthorized_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.UNAUTHORIZED)

    def get_forbidden_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.FORBIDDEN)

    def get_not_found_link(self):
        return self.driver.find_element(By.XPATH, LinkLocators.NOT_FOUND)

    @allure.step('Click created link')
    def click_created_link(self):
        logger.info('Click created link')
        return self.get_created_link().click()

    @allure.step('Click bad request link')
    def click_bad_request(self):
        logger.info('Click bad request link')
        return self.get_bad_request_link().click()

    @allure.step('Click no content link')
    def click_no_content_link(self):
        logger.info('Click no content link')
        return self.get_no_content_link().click()

    @allure.step('Click moved link')
    def click_moved_link(self):
        logger.info('Click moved link')
        return self.get_moved_link().click()

    @allure.step('Click unauthorized link')
    def click_unauthorized_link(self):
        logger.info('Click unauthorized link')
        return self.get_unauthorized_link().click()

    @allure.step('Click forbidden link')
    def click_forbidden_link(self):
        logger.info('Click forbidden link')
        return self.get_forbidden_link().click()

    @allure.step('Click not found link')
    def click_not_found_link(self):
        logger.info('Click not found link')
        return self.get_not_found_link().click()

    @allure.step('Get response code')
    def get_response_code(self):
        return self.driver.find_element(By.XPATH, LinkLocators.RESPONSE_CODE).text

    @allure.step('Get response text')
    def get_response_text(self):
        return self.driver.find_element(By.XPATH, LinkLocators.RESPONSE_TEXT).text

    def send_and_check(self, link: str) -> tuple[Any, Any]:
        if link == 'Created':
            self.click_created_link()
        elif link == 'No Content':
            self.click_no_content_link()
        elif link == 'Moved':
            self.click_moved_link()
        elif link == 'Bad Request':
            self.click_bad_request()
        elif link == 'Unauthorized':
            self.click_unauthorized_link()
        elif link == 'Forbidden':
            self.click_forbidden_link()
        else:
            self.click_not_found_link()
        code = self.get_response_code()
        text = self.get_response_text()
        return code, text
