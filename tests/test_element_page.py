import allure
import logging

from conf.locators.elements_page_locators import TextBoxLocators
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
