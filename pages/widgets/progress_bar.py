"""Module with method for progres bar page"""

import logging

import allure

from conf.locators.widgets_page_locators import ProgressBarLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ProgressBarPage(BasePage):
    """A class progress bar page"""

    locators = ProgressBarLocators()

    @allure.step('Start progress')
    def start_progress(self):
        logger.info('Start progress')
        return self.element_is_visible(self.locators.START_STOP_BTN).click()

    @allure.step('Stop progress')
    def stop_progress(self):
        logger.info('Stop progress')
        return self.element_is_visible(self.locators.START_STOP_BTN).click()

    def get_progress_value(self, value):
        while self._check_progress(value=value) != value:
            pass
        self.stop_progress()
        return self.element_is_visible(self.locators.PROGRESS_BAR).text.strip().replace("%", "")

    def _check_progress(self, value):
        current = self.element_is_visible(self.locators.PROGRESS_BAR).text.strip().replace("%", "")
        logger.info(f'Current value: {current}, need: {value}')
        return current
