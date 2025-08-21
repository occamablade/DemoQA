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

class RadioButtonLocators:
    """
    Class with locators on the radio buttons page
    """
    RADIO_BUTTON_LINK = 'https://demoqa.com/radio-button'
    YES_BUTTON = '//label[@for="yesRadio"]'
    IMPRESSIVE_BUTTON = '//label[@for="impressiveRadio"]'
    NO_BUTTON = '//label[@for="noRadio"]'
    SELECTED = '//span[@class="text-success"]'

class WebTablesLocators:
    """
    Class with locators on the web tables page
    """
    WEB_TABLES_LINK = 'https://demoqa.com/webtables'
    ADD_BTN = '//button[@id="addNewRecordButton"]'
    FIRST_NAME = '//input[@id="firstName"]'
    LAST_NAME = '//input[@id="lastName"]'
    EMAIL = '//input[@id="userEmail"]'
    AGE = '//input[@id="age"]'
    SALARY = '//input[@id="salary"]'
    DEPARTAMENT = '//input[@id="department"]'
    SUBMIT_BTN = '//button[@id="submit"]'
    CLOSE_REGISTRATION_BTN = '//button[@class="close"]'
    DELETE_ROW_BTN = 'span[title="Delete"]'
    PEOPLE_LIST = '//div[@class="rt-tr-group"]'
    INPUT_SEARCH = 'input[id="searchBox"]'
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    EDIT_BTN = '//span[@title="Edit"]'
    REGISTRATION_FORM_ALL_LINES = '.mr-sm-2.form-control'