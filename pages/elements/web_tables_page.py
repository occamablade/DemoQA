import allure
import logging
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import WebTablesLocators
from generator.generator import generated_person
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class WebTablesPage(BasePage):

    @allure.step('Click on "Add" button')
    def click_add_btn(self):
        return self.driver.find_element(By.XPATH, WebTablesLocators.ADD_BTN).click()

    @allure.step('Click on "Submit" button')
    def click_submit_btn(self):
        return self.driver.find_element(By.XPATH, WebTablesLocators.SUBMIT_BTN).click()

    @allure.step('Click "Edit" button')
    def click_edit_btn(self):
        return self.driver.find_element(By.XPATH, WebTablesLocators.EDIT_BTN).click()

    @allure.step('Create new person')
    def create_new_person(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        return first_name, last_name, email, str(age), str(salary), department

    @allure.step('Complete registration form')
    def add_new_person(self):
        self.click_add_btn()
        first_name, last_name, email, age, salary, department = self.create_new_person()
        self.driver.find_element(By.XPATH, WebTablesLocators.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(By.XPATH, WebTablesLocators.LAST_NAME).send_keys(last_name)
        self.driver.find_element(By.XPATH, WebTablesLocators.EMAIL).send_keys(email)
        self.driver.find_element(By.XPATH, WebTablesLocators.AGE).send_keys(age)
        self.driver.find_element(By.XPATH, WebTablesLocators.SALARY).send_keys(salary)
        self.driver.find_element(By.XPATH, WebTablesLocators.DEPARTAMENT).send_keys(department)
        self.click_submit_btn()
        return first_name, last_name, age, email, salary, department

    @allure.step('Check person info')
    def check_person(self):
        data = []
        person_list = self.driver.find_elements(By.XPATH, WebTablesLocators.PEOPLE_LIST)
        for item in person_list:
            if len(item.text.replace(' ', '')) != 0:
                data.append(item.text.splitlines())
        return 'Data not found' if len(data) == 0 else data

    def search_some_person(self, key_word):
        return self.driver.find_element(By.CSS_SELECTOR, WebTablesLocators.INPUT_SEARCH).send_keys(key_word)

    def update_person_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.click_edit_btn()
        self.driver.find_element(By.XPATH, WebTablesLocators.FIRST_NAME).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(By.XPATH, WebTablesLocators.LAST_NAME).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.LAST_NAME).send_keys(last_name)
        self.driver.find_element(By.XPATH, WebTablesLocators.EMAIL).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.EMAIL).send_keys(email)
        self.driver.find_element(By.XPATH, WebTablesLocators.AGE).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.AGE).send_keys(age)
        self.driver.find_element(By.XPATH, WebTablesLocators.SALARY).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.SALARY).send_keys(salary)
        self.driver.find_element(By.XPATH, WebTablesLocators.DEPARTAMENT).clear()
        self.driver.find_element(By.XPATH, WebTablesLocators.DEPARTAMENT).send_keys(department)
        self.click_submit_btn()
        return first_name, last_name, str(age), email, str(salary), department

    def delete_person(self):
        return self.driver.find_element(By.CSS_SELECTOR, WebTablesLocators.DELETE_ROW_BTN).click()
