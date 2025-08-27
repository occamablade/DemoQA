"""Module with test for widgets page"""
import logging
import allure
import pytest
from deepdiff import DeepDiff
from conf.locators.widgets_page_locators import AutoCompleteLocators, AccordianLocators, DatePickerLocators, \
    SliderLocators
from pages.widgets.accordian import AccordianPage
from pages.widgets.auto_complete import AutoCompletePage
from pages.widgets.date_picker import DatePickerPage
from pages.widgets.slider import SliderPage

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

    @allure.epic('Test Date Picker')
    class TestDatePicker:

        @allure.feature('Testing Select Date')
        def test_select_date(self, driver):
            date_picker = DatePickerPage(driver, DatePickerLocators.DATE_PICKER_LINK)
            date_picker.open()
            input_date = date_picker.select_date()
            get_data = date_picker.get_date()
            assert input_date == get_data, 'Date not same'

        @allure.feature('Testing Select Date and Time')
        def test_select_date_time(self, driver):
            date_picker = DatePickerPage(driver, DatePickerLocators.DATE_PICKER_LINK)
            date_picker.open()
            input_date = date_picker.select_date_time()
            get_data = date_picker.get_date_time()
            assert input_date == get_data, 'Date and time not same'

    @allure.epic('Test Slider')
    class TestSlider:

        @pytest.mark.parametrize('move', ['0', '25', '50', '75', '100'])
        @allure.feature('Testing Slider')
        def test_slider(self, driver, move):
            slider = SliderPage(driver, SliderLocators.SLIDER_LINK)
            slider.open()
            slider.set_slider_value(move)
            assert slider.get_slider_value() == move, 'Slider value not same'