"""Module with test for widgets page"""
import logging
import allure
import pytest
from deepdiff import DeepDiff
from conf.locators.widgets_page_locators import AutoCompleteLocators, AccordianLocators
from pages.widgets.accordian import AccordianPage
from pages.widgets.auto_complete import AutoCompletePage

logger = logging.getLogger(__name__)

@allure.suite('Widgets page')
class TestWidgetsPage:

    @allure.epic('Test Accordian')
    class TestAccordian:

        @pytest.mark.parametrize('section', ['1', '2', '3'])
        @allure.feature('Testing Accordian page')
        def test_accordian_page(self, driver, section):
            forms_page = AccordianPage(driver, AccordianLocators.ACCORDIAN_LINK)
            forms_page.open()
            assert forms_page.check_accordian_page(section=section) is not None, \
                'Text on open section not present'

    @allure.epic('Test Auto Complete')
    class TestAutoComplete:

        @allure.feature('Testing multiple autocomplete')
        def test_multiple(self, driver):
            auto_complete = AutoCompletePage(driver, AutoCompleteLocators.AUTO_COMPLETE_LINK)
            auto_complete.open()
            input_colors = auto_complete.set_multiple_colors()
            get_colors = auto_complete.get_multiple_colors()
            assert input_colors == get_colors, f'Colors not same, differense {DeepDiff(input_colors, get_colors)}'

        @allure.feature('Testing singe autocomplete')
        def test_single(self, driver):
            auto_complete = AutoCompletePage(driver, AutoCompleteLocators.AUTO_COMPLETE_LINK)
            auto_complete.open()
            input_colors = auto_complete.set_single_color()
            get_colors = auto_complete.get_single_color()
            assert input_colors == get_colors, f'Color not same, differense {DeepDiff(input_colors, get_colors)}'
