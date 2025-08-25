"""Module with method for browser windows page"""

import logging

import allure

from conf.locators.alerts_frame_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AlertsFrameWindowsPage(BasePage):
    """A class alerts and frame page"""
    locators = BrowserWindowsLocators()

    @allure.step('Open New Tab')
    def new_tab_page(self):
        self.element_is_visible(self.locators.NEW_TAB_BTN).click()
        logger.info('Click New Tab Button')
        self.go_to_a_new_tab()
        page_text = self.element_is_visible(self.locators.SAMPLE).text
        logger.info(page_text)
        return page_text

    @allure.step('Open New Window')
    def new_window_page(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BTN).click()
        logger.info('Click New Window Button')
        self.go_to_a_new_tab()
        page_text = self.element_is_visible(self.locators.SAMPLE).text
        logger.info(page_text)
        return page_text
