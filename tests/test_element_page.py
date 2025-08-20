import allure
import logging

import pytest

from conf.locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.radio_button_page import RadioButtonPage
from pages.elements.text_box_page import TextBoxPage

logger = logging.getLogger(__name__)

@allure.suite('Elements page')
class TestElementsPage:

    @allure.epic('Text Box')
    class TestTextBox:

        @allure.feature('Text Box')
        @allure.step('Check Text Box')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, TextBoxLocators.TEXT_BOX_LINK)
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            text_box_page.click_submit()
            cur_data = text_box_page.get_cur_fields()
            assert input_data == cur_data, 'failed'

    @allure.epic('Check Box')
    class TestCheckBox:

        @allure.feature('Check Box')
        @allure.step('Check Box')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, CheckBoxLocators.CHECK_BOX_LINK)
            check_box_page.open()
            check_box_page.random_click()
            selected_checkboxes = check_box_page.get_selected_checkboxes()
            logger.info(f'Selected checkboxes: {selected_checkboxes}')
            selected_fields = check_box_page.get_selected_fields()
            logger.info(f'Selected fields: {selected_fields}')
            assert selected_checkboxes == selected_fields, 'failed'

    @allure.epic('Radio button')
    class TestRadioButton:

        @allure.feature('Check valid choice in Radio Button')
        @pytest.mark.parametrize('choice', ['Yes', 'Impressive'])
        def test_valid_radio_button(self, driver, choice):
            radio_btn = RadioButtonPage(driver, RadioButtonLocators.RADIO_BUTTON_LINK)
            radio_btn.open()
            radio_btn.click_valid(choice)
            res = radio_btn.get_output_result()
            logger.info(f'Result: {res}')
            assert res == choice, 'failed'

        @pytest.mark.xfail
        @allure.feature('Check invalid choice in Radio Button')
        def test_invalid_radio_button(self, driver):
            radio_btn = RadioButtonPage(driver, RadioButtonLocators.RADIO_BUTTON_LINK)
            radio_btn.open()
            radio_btn.click_no()
            res = radio_btn.get_output_result()
            logger.info(f'Result: {res}')
            assert res == 'No', 'failed'
