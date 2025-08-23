"""Module with test for forms page"""

import allure

from conf.locators.forms_page_locators import FormsLocators
from pages.forms.forms import FormsPage


@allure.suite('Forms page')
class TestFormsPage(object):

    @allure.epic('Test Forms')
    class TestForms(object):

        @allure.feature('Check test form input and output data')
        def test_form_input_and_output_data(self, driver):
            forms_page = FormsPage(driver, FormsLocators.FORMS_LINK)
            forms_page.open()
            input_data = forms_page.fill_all_fields()
            result_data = forms_page.form_result()
            assert input_data == result_data, 'The entered data does not match the result'