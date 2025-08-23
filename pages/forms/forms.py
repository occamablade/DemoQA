"""Module with method for forms page"""

import os.path
import random
import logging

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.conf import Genders, Hobbies, Months, Timeouts
from conf.locators.forms_page_locators import FormsLocators
from config import PROJECT_PATH
from generator.generator import generate_person, generate_subject
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class FormsPage(BasePage):
    """A class to forms page"""
    locators = FormsLocators()

    def fill_all_fields(self) -> list[str]:
        """
        Fill all fields in form page
        :return: data inputs
        """
        person = next(generate_person())
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        phone = random.randint(1000000000, 9999999999)
        current_address = person.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        logging.info(f'First name: {first_name}')

        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        logging.info(f'Last name: {last_name}')

        self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
        logging.info(f'Email: {email}')

        gender = self.choice_gender()
        logging.info(f'Gender: {gender}')

        self.element_is_visible(self.locators.MOBILE_NUBER).send_keys(phone)
        logging.info(f'Phone: {phone}')

        date_birth = self.choice_date_birth()
        logging.info(f'Date of Birth: {date_birth}')

        subjects = generate_subject()
        self.choice_subjects(subjects)
        subjects = ', '.join(subjects)
        logger.info(f'Subjects: {subjects}')

        hobbies = self.choice_hobbies()
        hobbies = ', '.join(hobbies)
        logging.info(f'Hobbies: {hobbies}')

        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(os.path.join(PROJECT_PATH,'conf\img\me.png'))
        logger.info('Picture is me.png')

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        logger.info(f'Current address: {current_address}')

        state_city = self.choice_state_city()
        logging.info(f'State and city: {state_city}')

        self.element_is_visible(self.locators.SUBMIT).click()
        data_input = [str(first_name + ' ' + last_name), email, str(gender), str(phone),
                      date_birth, subjects, hobbies, 'me.png', current_address, state_city]
        logger.critical(data_input)
        return data_input

    @allure.step('Check registration form')
    def form_result(self) -> list[str]:
        """
        Get a result complete registration form
        :return:
        """
        result_list = self.elements_are_present(self.locators.TABLE_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        logger.critical(data)
        return data

    @allure.step('Select gender')
    def choice_gender(self) -> str:
        """
        Method to choose gender from gender list
        :return: gender (Male|Female|Other)
        """
        choice = random.randint(1, 3)
        gender = Genders.genders[str(choice)]
        if gender == 'Male':
            self.element_is_visible(self.locators.SELECT_MALE_GENDER).click()
            return gender
        elif gender == 'Female':
            self.element_is_visible(self.locators.SELECT_FEMALE_GENDER).click()
            return gender
        self.element_is_visible(self.locators.SELECT_OTHER_GENDER).click()
        return gender

    @allure.step('Select hobbies')
    def choice_hobbies(self) -> list[str]:
        """
        Method to choose hobby from hobbies list
        :return: list of choiced hoobies (1-3) (Sports|Reading|Music)
        """
        count = random.randint(1, 3)
        choiced = []
        for i in range(0, count + 1):
            choice = random.randint(1, 3)
            hobbies = Hobbies.hobbies[str(choice)]
            if hobbies in choiced:
                break
            elif hobbies == 'Sports':
                self.element_is_visible(self.locators.HOBBIES_SPORTS).click()
                choiced.append(hobbies)
            elif hobbies == 'Reading':
                self.element_is_visible(self.locators.HOBBIES_READING).click()
                choiced.append(hobbies)
            else:
                self.element_is_visible(self.locators.HOBBIES_MUSIC).click()
                choiced.append(hobbies)
        return choiced

    @allure.step('Select date of birth')
    def choice_date_birth(self) -> str:
        """
        Method to generate and input date of birth
        :return: str (day month,year)
        """
        month = random.randint(0, 11)
        year = random.randint(1980, 2020)
        day = random.randint(1, 25)

        self.element_is_visible(self.locators.DATE_BIRTH).click()

        month_select = Select(self.element_is_visible(self.locators.MONTH))
        month_select.select_by_value(str(month))

        year_select = Select(self.element_is_visible(self.locators.YEAR))
        year_select.select_by_value(str(year))

        day_locator = (By.XPATH, FormsLocators.DAY.format(day))
        self.element_is_visible(day_locator).click()

        return str(day) + ' ' + Months.months[str(month)] + ',' + str(year)

    @allure.step('Select state and city')
    def choice_state_city(self) -> str:
        """
        Method to generate and input state and city
        :return: str (state city)
        """
        self.element_is_visible(self.locators.STATE_DROPDOWN).click()
        state_options = WebDriverWait(self.driver, Timeouts.sec_10).until(
            EC.visibility_of_all_elements_located(self.locators.STATE_OPTIONS)
        )
        random_state = random.choice(state_options[1:] if len(state_options) > 1 else state_options)
        state_name = random_state.text
        random_state.click()
        WebDriverWait(self.driver, Timeouts.sec_10).until(
            EC.element_to_be_clickable(self.locators.CITY_DROPDOWN)
        )
        self.element_is_visible(self.locators.CITY_DROPDOWN).click()
        city_options = WebDriverWait(self.driver, Timeouts.sec_10).until(
            EC.visibility_of_all_elements_located(self.locators.CITY_OPTIONS)
        )
        random_city = random.choice(city_options[1:] if len(city_options) > 1 else city_options)
        city_name = random_city.text
        random_city.click()
        return f'{state_name} {city_name}'

    @allure.step('Select subjects')
    def choice_subjects(self, subjects: list) -> None:
        """
        Method to choose subjects from subjects list
        :param subjects: list of subjects
        :return: None
        """
        self.element_is_visible(self.locators.SUBJECTS).click()
        for subject in subjects:
            self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
