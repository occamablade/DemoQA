"""Module with locators on the alerts, frame and windows page"""
from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    """
    Class with locators on the browser windows page
    """
    BROWSER_WINDOWS_LINK = 'https://demoqa.com/browser-windows'
    NEW_TAB_BTN = (By.XPATH, '//button[@id="tabButton"]')
    NEW_WINDOW_BTN = (By.XPATH, '//button[@id="windowButton"]')
    NEW_WINDOW_MSG_BTN = (By.XPATH, '//button[@id="messageWindowButton"]')
    SAMPLE = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_MSG = (By.XPATH, '/html/body/text()')

class AlertsPageLocators:
    """Class with locators on the alerts page"""
    ALERTS_LINK = 'https://demoqa.com/alerts'
    ALERT_BTN = (By.XPATH, '//button[@id="alertButton"]')
    TIMER_ALERT_BTN = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BTN_ALERT = (By.XPATH, '//button[@id="confirmButton"]')
    RESULT_CONFIRM_ALERT = (By.XPATH, '//span[@id="confirmResult"]')
    LOGIN_ALERT_BTN = (By.XPATH, '//button[@id="promtButton"]')
    PROMT_ALERT_RESULT = (By.XPATH, '//span[@id="promptResult"]')

class FramePageLocators:
    """Class with locators on the frames page"""
    FRAME_LINK = 'https://demoqa.com/frames'
    BIG_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    SMALL_FRAME = (By.XPATH, '//iframe[@id="frame2"]')
    TITLE_FRAME = (By.XPATH, '//h1[@id="sampleHeading"]')

class NestedFramePageLocators:
    """Class with locators on the nested frames page"""
    NESTED_FRAME_LINK = 'https://demoqa.com/nestedframes'
    PARENT_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogPageLocators:
    """Class with locators on the modal dialog page"""
    MODAL_DIALOG_LINK = 'https://demoqa.com/modal-dialogs'
    SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    SMALL_MODAL_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-sm"]')
    SMALL_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_SMALL_MODAL = (By.XPATH, "//button[@id='closeSmallModal']")
    LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")
    LARGE_MODAL_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')
    LARGE_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    CLOSE_LARGE_MODAL = (By.XPATH, "//button[@id='closeLargeModal']")
