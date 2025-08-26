"""Module with method for date picker page"""

import logging
import random

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from conf.conf import Months
from conf.locators.widgets_page_locators import DatePickerLocators
from generator.generator import generate_time
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


def convert_time(time: str) -> str:
    hours, minutes = time.split(':')
    hours_int = int(hours)
    if hours_int == 0:
        return f"12:{minutes} AM"
    elif hours_int < 12:
        return f"{hours_int}:{minutes} AM"
    elif hours_int == 12:
        return f"12:{minutes} PM"
    else:
        return f"{hours_int - 12}:{minutes} PM"


class DatePickerPage(BasePage):
    """A class date picker page"""

    locators = DatePickerLocators()

    @allure.step('Select date')
    def select_date(self) -> str:
        """
        Method to generate and input date of birth
        :return: str (month/day/year)
        """
        month = random.randint(0, 11)
        year = random.randint(1980, 2020)
        day = random.randint(1, 25)

        self.element_is_visible(self.locators.DATE_INPUT).click()

        month_select = Select(self.element_is_visible(self.locators.MONTH))
        month_select.select_by_value(str(month))

        year_select = Select(self.element_is_visible(self.locators.YEAR))
        year_select.select_by_value(str(year))

        day_locator = (By.XPATH, DatePickerLocators.DAY.format(day))
        self.element_is_visible(day_locator).click()

        month = str(month + 1) if len(str(month + 1)) == 2 else str('0' + f'{str(month + 1)}')
        day = str(day) if len(str(day)) == 2 else str('0' + f'{str(day)}')

        return month + '/' + str(day) + '/' + str(year)

    @allure.step('Get Select date')
    def get_date(self) -> str:
        return str(self.element_is_visible(self.locators.DATE_INPUT).get_attribute('value'))

    @allure.step('Select date and time')
    def select_date_time(self):
        time, apm = generate_time()
        month = random.randint(0, 11)
        year = 2023
        day = random.randint(1, 28)

        self.element_is_visible(self.locators.DATE_TIME_INPUT).click()

        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        month_options = self.elements_are_present(self.locators.MONTHS_OPTIONS)
        month_options[month].click()

        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        year_elements = self.elements_are_visible(self.locators.YEAR_OPTION)

        target_year = None
        for year_element in year_elements:
            if year_element.text == str(year):
                target_year = year_element
                break

        if target_year:
            self.go_to_element(target_year)
            target_year.click()
        else:
            raise ValueError(f"Year {year} not found in dropdown")

        days = self.elements_are_visible(self.locators.DAY_SELECTED)
        for day_element in days:
            if day_element.text == str(day):
                day_element.click()
                break

        time_elements = self.elements_are_visible(self.locators.DATE_TIME_TIME)
        for time_element in time_elements:
            if time in time_element.text:
                time_element.click()
                break

        time = convert_time(time)
        logger.info(f'Choiced time: {time}')
        logger.info(f'Choiced month: {month}')
        logger.info(f'Choiced year: {year}')
        logger.info(f'Choiced day: {day}')
        month_name = Months.months[str(month)]
        return f"{month_name} {day}, {year} {time}"

    @allure.step('Get Select date and time')
    def get_date_time(self) -> str:
        return str(self.element_is_visible(self.locators.DATE_TIME_INPUT).get_attribute('value'))
