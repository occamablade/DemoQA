"""Module with locators on the forms page"""

from selenium.webdriver.common.by import By


class FormsLocators:
    """
    Class with locators on the forms page
    """
    FORMS_LINK = 'https://demoqa.com/automation-practice-form'
    FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    USER_EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    SELECT_MALE_GENDER = (By.XPATH, '//label[@for="gender-radio-1"]')
    SELECT_FEMALE_GENDER = (By.XPATH, '//label[@for="gender-radio-2"]')
    SELECT_OTHER_GENDER = (By.XPATH, '//label[@for="gender-radio-3"]')
    MOBILE_NUBER = (By.XPATH, '//input[@id="userNumber"]')
    DATE_BIRTH = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    SUBJECTS = (By.XPATH, '//input[@id="subjectsInput"]')
    HOBBIES_SPORTS = (By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    HOBBIES_READING = (By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    HOBBIES_MUSIC = (By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    UPLOAD_PICTURE = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//div[@id="state"]')
    INPUT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    STATE_TEXT = (By.XPATH, '//*[@id="state"]/div/div[1]/div[1]')
    SELECT_CITY = (By.XPATH, '//div[@id="city"]')
    INPUT_CITY = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    CITY_TEXT = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    STATE_DROPDOWN = (By.CSS_SELECTOR, "#state")
    STATE_OPTIONS = (By.CSS_SELECTOR, "#state div[class*='option']")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "#city")
    CITY_OPTIONS = (By.CSS_SELECTOR, "#city div[class*='option']")

    MONTH = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    YEAR = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    DAY = "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{}']"

    TABLE_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
