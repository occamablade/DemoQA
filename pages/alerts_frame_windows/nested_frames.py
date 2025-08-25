"""Module with method for nested page"""

import logging

import allure

from conf.locators.alerts_frame_windows_locators import NestedFramePageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class NestedFramesPage(BasePage):
    """A class nested frames page"""
    locators = NestedFramePageLocators()

    @allure.step('Check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.go_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        logger.info(f'Parent frame text: {parent_text}')
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.go_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        logger.info(f'Child frame text: {child_text}')
        return parent_text, child_text
