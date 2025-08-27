"""Module with method for slider page"""

import logging

import allure

from conf.locators.widgets_page_locators import SliderLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class SliderPage(BasePage):
    """A class slider page"""

    locators = SliderLocators()

    @allure.step('Move slider')
    def set_slider_value(self, move_to: str) -> str:
        """Move slider to new value
        :param move_to: value to move to
        :return: value to move to"""
        slider = self.element_is_visible(self.locators.SLIDER)
        current_value = int(slider.get_attribute("value"))
        logger.info(f'Slider value : {current_value}')
        logger.info(f'Move slider on value : {move_to}')
        self.driver.execute_script("arguments[0].value = arguments[1];", slider, move_to)
        return move_to

    @allure.step('Get value slider')
    def get_slider_value(self) -> str:
        """
        Get value slider
        :return: string value
        """
        value = self.element_is_visible(self.locators.SLIDER_VALUE_BOX).get_attribute('value')
        logger.info(f'Slider value : {value}')
        return str(value)
