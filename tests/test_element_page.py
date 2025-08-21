import random

import allure
import logging

import pytest

from conf.locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, \
    WebTablesLocators, ButtonLocators
from pages.elements.button_page import ButtonPage
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.radio_button_page import RadioButtonPage
from pages.elements.text_box_page import TextBoxPage
from pages.elements.web_tables_page import WebTablesPage

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
            assert input_data == cur_data, 'Input and output datas not same'

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
            assert selected_checkboxes == selected_fields, 'Checkboxes have not been selected'

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
            assert res == choice, 'Valid click on radio button not complete'

        @pytest.mark.xfail
        @allure.feature('Check invalid choice in Radio Button')
        def test_invalid_radio_button(self, driver):
            radio_btn = RadioButtonPage(driver, RadioButtonLocators.RADIO_BUTTON_LINK)
            radio_btn.open()
            radio_btn.click_no()
            res = radio_btn.get_output_result()
            logger.info(f'Result: {res}')
            assert res == 'No', 'Invalid click on radio button complete'

    @allure.epic('Web Tables')
    class TestWebTables:

        @allure.feature('Add new perwon')
        def test_add_person_web_tables(self, driver):
            web_tables = WebTablesPage(driver, WebTablesLocators.WEB_TABLES_LINK)
            web_tables.open()
            new_person = list(web_tables.add_new_person())
            logger.info(f'New person data: {new_person}')
            output_data = web_tables.check_person()
            assert new_person in output_data, 'New person not in output data'

        @allure.feature('Search person')
        def test_search_person_web_tables(self, driver):
            web_tables = WebTablesPage(driver, WebTablesLocators.WEB_TABLES_LINK)
            web_tables.open()
            new_person = list(web_tables.add_new_person())
            search_word = new_person[random.randint(0, len(new_person) - 1)]
            logger.info(f'Search person data: {search_word}')
            web_tables.search_some_person(search_word)
            output_data = web_tables.check_person()
            assert new_person in output_data, 'New person not found in the table after search'
            for person in output_data:
                assert search_word in person, f'{search_word} not found in person data'

        @allure.feature('Edit person')
        def test_edit_person_web_tables(self, driver):
            web_tables = WebTablesPage(driver, WebTablesLocators.WEB_TABLES_LINK)
            web_tables.open()
            edit_person = list(web_tables.update_person_info())
            logger.info(f'Edit person info: {edit_person}')
            output_data = web_tables.check_person()
            logger.info(f'Check person info: {output_data}')
            assert edit_person in output_data, 'Edit person not found in the table after editing'

        @allure.feature('Delete person')
        def test_delete_person_web_tables(self, driver):
            web_tables = WebTablesPage(driver, WebTablesLocators.WEB_TABLES_LINK)
            web_tables.open()
            before_delete = web_tables.check_person()
            web_tables.delete_person()
            after_delete = web_tables.check_person()
            assert len(before_delete) > len(after_delete), 'Person not deleted'

    @allure.epic('Button page')
    class TestButtonPage:

        @pytest.mark.parametrize('type_click', ['double', 'right', 'dynamic'])
        @allure.feature('Check "click" button')
        def test_check_click_button(self, driver, type_click):
            button_page = ButtonPage(driver, ButtonLocators.BUTTON_LINK)
            button_page.open()
            assert button_page.click_and_check(type_click=type_click) == f'You have done a {type_click} click', \
                f'{type_click} was not pressed'