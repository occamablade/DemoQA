import allure
import logging
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import TextBoxLocators
from generator.generator import generate_person
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class TextBoxPage(BasePage):

    @allure.step('Fill all fields')
    def fill_all_fields(self):
        person_info = next(generate_person())

        full_name = self.driver.find_element(By.XPATH, TextBoxLocators.FULL_NAME)
        full_name.send_keys(person_info.full_name)
        email = self.driver.find_element(By.XPATH, TextBoxLocators.EMAIL)
        email.send_keys(person_info.email)
        current_address = self.driver.find_element(By.XPATH, TextBoxLocators.CURRENT_ADDRESS)
        current_address.send_keys(person_info.current_address)
        permanent_address = self.driver.find_element(By.XPATH, TextBoxLocators.PERMANENT_ADDRESS)
        permanent_address.send_keys(person_info.permanent_address)
        logger.info(f'Full name is {person_info.full_name}')
        logger.info(f'Email is {person_info.email}')
        logger.info(f'Current address is {person_info.current_address}')
        logger.info(f'Premanent address is {person_info.permanent_address}')
        return person_info.full_name, person_info.email, person_info.current_address, person_info.permanent_address

    @allure.step('Check fill fields')
    def get_cur_fields(self):
        cur_full_name = self.driver.find_element(By.XPATH, TextBoxLocators.CUR_FULL_NAME).text.split(':')[1]
        cur_email = self.driver.find_element(By.XPATH, TextBoxLocators.CUR_EMAIL).text.split(':')[1]
        cur_current_address = self.driver.find_element(By.XPATH, TextBoxLocators.CUR_CURRENT_ADDRESS).text.split(':')[1]
        cur_permanent_address = self.driver.find_element(By.XPATH, TextBoxLocators.CUR_PERMANENT_ADDRESS).text.split(':')[1]
        logger.info(f'Sending full name is {cur_full_name}')
        logger.info(f'Sending email is {cur_email}')
        logger.info(f'Sending current address is {cur_current_address}')
        logger.info(f'Sendinf permanent address is {cur_permanent_address}')
        return cur_full_name, cur_email, cur_current_address, cur_permanent_address

    @allure.step('Click submit button')
    def click_submit(self):
        logger.info('Click submit button')
        btn = self.driver.find_element(By.XPATH, TextBoxLocators.BUTTON_SUBMIT)
        return btn.click()
