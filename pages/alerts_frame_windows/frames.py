"""Module with method for frames page"""

import logging

import allure

from conf.locators.alerts_frame_windows_locators import FramePageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class FramesPage(BasePage):
    """A class frame page"""
    locators = FramePageLocators()

    @allure.step('Check big frame size')
    def check_big_frmae(self):
        frame = self.element_is_present(self.locators.BIG_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        logger.info(f'Big frame width: {width}')
        logger.info(f'Big frame height: {height}')
        self.go_to_frame(frame)
        text = self.element_is_visible(self.locators.TITLE_FRAME).text
        logger.info(f'Big frame text: {text}')
        self.switch_to_default_content()
        return [text, width, height]

    @allure.step('Check small frame size')
    def check_small_frame(self):
        frame = self.element_is_present(self.locators.SMALL_FRAME)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        logger.info(f'Small frame width: {width}')
        logger.info(f'Small frame height: {height}')
        self.go_to_frame(frame)
        text = self.element_is_visible(self.locators.TITLE_FRAME).text
        logger.info(f'Small frame text: {text}')
        self.switch_to_default_content()
        return [text, width, height]
