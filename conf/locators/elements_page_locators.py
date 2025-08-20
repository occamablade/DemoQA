"""Module with locators on the elements page"""

class TextBoxLocators:
    """
    Class with locators on the text box page
    """

    TEXT_BOX_LINK = 'https://demoqa.com/text-box'
    FULL_NAME = "//input[@id='userName']"
    EMAIL =  "//input[@id='userEmail']"
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    BUTTON_SUBMIT = "//button[@id='submit']"

    CUR_FULL_NAME = "//p[@id='name']"
    CUR_EMAIL = "//p[@id='email']"
    CUR_CURRENT_ADDRESS = "//p[@id='currentAddress']"
    CUR_PERMANENT_ADDRESS = "//p[@id='permanentAddress']"

class CheckBoxLocators:
    """
    Class with locators on the checkbox page
    """
    CHECK_BOX_LINK = 'https://demoqa.com/checkbox'
    EXPAND_ALL = '//button[@title="Expand all"]'
    COLLAPSE_ALL = '//button[@title="Collapse all"]'
    SELECT_ALL = '//span[@class="rct-checkbox"]'
    SELECTED = '//span[@class="text-success"]'
    CURRENT_SELECTED = 'svg[class="rct-icon rct-icon-check"]'
    ALL_FIELDS = '//span[@class="rct-title"]'
    TITLE_TEXT = './/ancestor::span[@class="rct-text"]'
