"""Module with test for widgets page"""
import logging
import allure
import pytest

from conf.locators.widgets_page_locators import AccordianLocators
from pages.widgets.accordian import AccordianPage

logger = logging.getLogger(__name__)

@allure.suite('Widgets page')
class TestWidgetsPage(object):

    @allure.epic('Test Accordian')
    class TestAccordian(object):

        @pytest.mark.parametrize('section', ['1', '2', '3'])
        @allure.feature('Testing Accordian page')
        def test_accordian_page(self, driver, section):
            forms_page = AccordianPage(driver, AccordianLocators.ACCORDIAN_LINK)
            forms_page.open()
            assert forms_page.check_accordian_page(section=section) is not None, \
                'Text on open section not present'

