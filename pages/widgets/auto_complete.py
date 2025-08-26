"""Module with method for auto complete page"""

import logging
import random

import allure
from selenium.webdriver import Keys

from conf.conf import Colors
from conf.locators.widgets_page_locators import AutoCompleteLocators
from generator.generator import generate_color
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AutoCompletePage(BasePage):
    """A class auto complete page"""

    locators = AutoCompleteLocators()

    @allure.step('Set multiple color names')
    def set_multiple_colors(self) -> list[str]:
        colors = list(generate_color(count=random.randint(1, len(Colors.colors) + 1)))
        logger.info(f'Selected colors: {colors}')
        for color in colors:
            input_multi = self.elements_is_clickable(self.locators.INPUT_MULTI)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('Get mulriple colors')
    def get_multiple_colors(self) -> list[str]:
        color_list = self.elements_are_present(self.locators.LIST_MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        logger.info(f'Get colors: {colors}')
        return colors

    @allure.step('Set single color')
    def set_single_color(self) -> str:
        color = list(generate_color(count=1))[0]
        logger.info(f'Selected color: {color}')
        input_single = self.elements_is_clickable(self.locators.INPUT_SINGLE)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    @allure.step('Get single colors')
    def get_single_color(self) -> str:
        color = str(self.element_is_visible(self.locators.SINGLE_CONTAINER).text)
        logger.info(f'Get color: {color}')
        return color
