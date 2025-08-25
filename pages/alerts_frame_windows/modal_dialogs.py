"""Module with method for modal dialogs page"""

import logging

import allure

from conf.locators.alerts_frame_windows_locators import ModalDialogPageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ModalDialogsPage(BasePage):
    """A class modal dialogs page"""
    locators = ModalDialogPageLocators()

    @allure.step('Check small modal window')
    def check_small_modal_window(self):
        logger.info('Click Small Modal')
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        modal_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        logger.info(f'Modal Title: {modal_title}')
        logger.info(f'Modal Text: {modal_text}')
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()
        logger.info('Click Close Modal')
        return modal_title, modal_text

    @allure.step('Check large modal window')
    def check_large_modal_window(self):
        logger.info('Click Large Modal')
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        modal_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        modal_text = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        logger.info('Click Close Modal')
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()
        logger.info(f'Modal Title: {modal_title}')
        logger.info(f'Modal Text Length: {len(modal_text)}')
        return modal_title, len(modal_text)
