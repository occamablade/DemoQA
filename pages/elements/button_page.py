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
            self.action_double_click(self.driver.find_element(By.CSS_SELECTOR, ButtonLocators.DOUBLE_CLICK_BTN))
            return self.driver.find_element(By.CSS_SELECTOR, ButtonLocators.DOUBLE_CLICK_MESSAGE).text
        elif type_click == 'right':
            self.action_right_click(self.driver.find_element(By.CSS_SELECTOR, ButtonLocators.RIGHT_CLICK_BTN))
            return self.driver.find_element(By.CSS_SELECTOR, ButtonLocators.RIGHT_MESSAGE).text
        else:
            self.driver.find_element(By.XPATH, ButtonLocators.CLICK_BTN).click()
            return self.driver.find_element(By.CSS_SELECTOR, ButtonLocators.CLICK_ME_MESSAGE).text
