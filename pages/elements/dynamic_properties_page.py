import logging
import time

from selenium.common import TimeoutException


from conf.conf import Timeouts
from conf.locators.elements_page_locators import DynamicPropertiesLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()
    def check_enable_button(self):
        try:
            logger.info('Checking if an element is enable')
            self.elements_is_clickable(self.locators.ENABLE_AFTER_BTN).click()
        except TimeoutException:
            return False
        return True

    def check_appear_button(self):
        try:
            logger.info('Checking if an element is visible')
            self.element_is_visible(self.locators.VISIBLE_AFTER_BTN)
        except TimeoutException:
            return False
        return True

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BTN)
        color_button_before = color_button.value_of_css_property('color')
        logger.info('Initial button color: ', color_button_before)
        time.sleep(Timeouts.sec_10)
        color_button_after = color_button.value_of_css_property('color')
        logger.info('Button color after clicking: ', color_button_after)
        return color_button_before, color_button_after