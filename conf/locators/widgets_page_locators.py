"""Module with locators on the accordian page"""

from selenium.webdriver.common.by import By


class AccordianLocators:
    """
    Class with locators on the accordian page
    """
    ACCORDIAN_LINK = 'https://demoqa.com/accordian'
    TAB = '//*[@id="section{}Heading"]'
    TEXT = '//div[@id="section{}Content"]/p'


class AutoCompleteLocators:
    """
    Class with locators on the auto complete page
    """
    AUTO_COMPLETE_LINK = 'https://demoqa.com/auto-complete'
    INPUT_MULTI = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    INPUT_SINGLE = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')
    LIST_MULTI_VALUE = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    SINGLE_CONTAINER = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')

class DatePickerLocators:
    """
    Class with locators on the date picker page
    """
    DATE_PICKER_LINK = 'https://demoqa.com/date-picker'
    DATE_INPUT = (By.XPATH, '//input[@id="datePickerMonthYearInput"]')

    MONTHS_OPTIONS = (By.CSS_SELECTOR, '.react-datepicker__month-option')
    YEAR_OPTION = (By.CSS_SELECTOR, '.react-datepicker__year-option')

    DATE_TIME_INPUT = (By.XPATH, '//input[@id="dateAndTimePickerInput"]')
    DATE_TIME_MONTH = (By.CLASS_NAME, 'react-datepicker__month-read-view')
    DATE_TIME_YEAR = (By.CSS_SELECTOR, '.react-datepicker__year-read-view')
    DATE_TIME_TIME = (By.CSS_SELECTOR, '.react-datepicker__time-list-item')

    MONTH = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    YEAR = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    DAY = "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{}']"

    DAY_SELECTED = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month'))]")

class SliderLocators:
    """
    Class with locators on the slider page
    """
    SLIDER_LINK = 'https://demoqa.com/slider'
    SLIDER = (By.ID, "sliderValue")
    SLIDER_VALUE_BOX = (By.CSS_SELECTOR, "#sliderValue")

class ProgressBarLocators:
    """
    Class with locators on the progress bar page
    """
    PROGRESS_BAR_LINK = 'https://demoqa.com/progress-bar'
    START_STOP_BTN = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.ID, "progressBar")
    RESET_BTN = (By.ID, "resetButton")
