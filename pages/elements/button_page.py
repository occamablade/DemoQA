import logging

import allure
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import ButtonLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ButtonPage(BasePage):

    @allure.step('Click')
    def click_and_check(self, type_click):
        if type_click == 'double':
            self.mouse_double_click(ButtonLocators.DOUBLE_CLICK_BTN)
            return self.driver.find_element(By.XPATH, ButtonLocators.DOUBLE_CLICK_MESSAGE).text
        elif type_click == 'right':
            self.mouse_right_click(ButtonLocators.RIGHT_CLICK_BTN)
            return self.driver.find_element(By.XPATH, ButtonLocators.RIGHT_MESSAGE).text
        else:
            self.mouse_click(ButtonLocators.CLICK_BTN)
            return self.driver.find_element(By.XPATH, ButtonLocators.CLICK_ME_MESSAGE).text
