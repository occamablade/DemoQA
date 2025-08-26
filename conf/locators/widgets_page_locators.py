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
