import allure
import logging

from conf.locators.elements_page_locators import TextBoxLocators, CheckBoxLocators
from pages.elements.check_box_page import CheckBoxPage
from pages.elements.text_box_page import TextBoxPage

logger = logging.getLogger(__name__)

@allure.suite('Elements page')
class TestElementsPage:

    @allure.feature('Text Box')
    class TestTextBox:

        @allure.step('Check Text Box')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, TextBoxLocators.TEXT_BOX_LINK)
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            text_box_page.click_submit()
            cur_data = text_box_page.get_cur_fields()
            assert input_data == cur_data, 'failed'

    @allure.feature('Check Box')
    class TestCheckBox:

        @allure.step('Check Check Box')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, CheckBoxLocators.CHECK_BOX_LINK)
            check_box_page.open()
            check_box_page.random_click()
            selected_checkboxes = check_box_page.get_selected_checkboxes()
            logger.info(f'Selected checkboxes: {selected_checkboxes}')
            selected_fields = check_box_page.get_selected_fields()
            logger.info(f'Selected fields: {selected_fields}')
            assert selected_checkboxes == selected_fields, 'failed'