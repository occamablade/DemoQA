"""Module with locators on the accordian page"""

from selenium.webdriver.common.by import By


class AccordianLocators:
    """
    Class with locators on the accordian page
    """
    ACCORDIAN_LINK = 'https://demoqa.com/accordian'

    TAB = '//*[@id="section{}Heading"]'
    TEXT = '//div[@id="section{}Content"]/p'

