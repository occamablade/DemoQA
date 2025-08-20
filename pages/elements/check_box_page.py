import random

import allure
import logging
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import CheckBoxLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class CheckBoxPage(BasePage):

    @allure.step('Expand all fields')
    def expand_all(self):
        logger.info('Expand all fields')
        return self.driver.find_element(By.XPATH, CheckBoxLocators.EXPAND_ALL).click()

    @allure.step('Collapse all fields')
    def collapse_all(self):
        logger.info('Collapse all fields')
        return self.driver.find_element(By.XPATH, CheckBoxLocators.COLLAPSE_ALL).click()

    @allure.step('Select all fields')
    def select_all(self):
        logger.info('Select all fields')
        return self.driver.find_element(By.XPATH, CheckBoxLocators.SELECT_ALL).click()

    @allure.step('Get selected fields')
    def get_selected_fields(self):
        logger.info('Get selected fields')
        selected = self.driver.find_elements(By.XPATH, CheckBoxLocators.SELECTED)
        data = []
        for element in selected:
            data.append(element.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        return data

    @allure.step('Randomly click on checkboxes')
    def random_click(self):
        logger.info('Randomly click on checkboxes')
        self.expand_all()
        fields = self.driver.find_elements(By.XPATH, CheckBoxLocators.ALL_FIELDS)
        data = []
        for field in fields:
            if random.randint(1, 2) == 1:
                field.click()
                data.append(field.text)

    @allure.step('Get selected checkboxes')
    def get_selected_checkboxes(self):
        logger.info('Get selected checkboxes')
        check_boxes = self.driver.find_elements(By.CSS_SELECTOR, CheckBoxLocators.CURRENT_SELECTED)
        data = []
        for check_box in check_boxes:
            title = check_box.find_element(By.XPATH, CheckBoxLocators.TITLE_TEXT)
            data.append(title.text)
        data = str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
        return data
