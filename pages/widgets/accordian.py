"""Module with method for widgets page"""

import logging

import allure
from selenium.webdriver.common.by import By

from conf.locators.widgets_page_locators import AccordianLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AccordianPage(BasePage):
    """A class nested accordian page"""

    locators = AccordianLocators()

    @allure.step('Click section')
    def click_section(self, section: str):
        """click title on accordian page
        :param section: section number
        :type section: str"""
        logger.info(f'Click section {section}')
        locator = (By.XPATH, AccordianLocators.TAB.format(section))
        return self.element_is_visible(locator).click()

    @allure.step('Get text from section')
    def get_text(self, section: str):
        """get text from accordian page
        :param section: section number
        :return: text from section"""
        logger.info('Get text from accordian page')
        locator = (By.XPATH, AccordianLocators.TEXT.format(section))
        return self.element_is_visible(locator).text

    @allure.step('Check accordian page')
    def check_accordian_page(self, section: str):
        """check accordian page
        :param section: section number
        :return: text from section"""
        logger.info(f'Check accordian page {section}')
        self.click_section(section=section)
        text = self.get_text(section=section)
        logger.info(f'Text from section {section} : {text}')
        return text