"""Module with method for tabs page"""

import logging

import allure

from conf.locators.widgets_page_locators import TabsLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class TabsPage(BasePage):
    """A class tabs page"""

    locators = TabsLocators()

    @allure.step('Click on tab')
    def click_tab(self, tab_name: str):
        """Click tab button"""
        logger.info(f'Click on tab {tab_name}')
        return self.element_is_visible(self.locators.TABS[tab_name]['locator']).click()

    @allure.step('Get text from tab')
    def get_text(self, tab_name: str) -> str:
        """Get text from tab button"""
        text_from_tab = self.element_is_visible(self.locators.TABS[tab_name]['text']).text.strip()
        logger.info(f'Get text from tab button: {text_from_tab}')
        return text_from_tab
