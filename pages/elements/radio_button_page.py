import allure
import logging
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import RadioButtonLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class RadioButtonPage(BasePage):

    @allure.step('Click valid radio button choice')
    def click_valid(self, choice):
        logger.info(f'Click {choice} radio button choice')
        if choice == 'Yes':
            return self.click_yes()
        return self.click_impressive()

    @allure.step('Click "Yes" radio button')
    def click_yes(self):
        return self.driver.find_element(By.XPATH, RadioButtonLocators.YES_BUTTON).click()

    @allure.step('Click "Impressive" radio button')
    def click_impressive(self):
        return self.driver.find_element(By.XPATH, RadioButtonLocators.IMPRESSIVE_BUTTON).click()

    @allure.step('Click "No" radio button')
    def click_no(self):
        return self.driver.find_element(By.XPATH, RadioButtonLocators.NO_BUTTON).click()

    @allure.step('Get output result of click')
    def get_output_result(self):
        logger.info('Get output result of click')
        result = self.driver.find_element(By.XPATH, RadioButtonLocators.SELECTED).text
        return result
