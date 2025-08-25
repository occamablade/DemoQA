"""Module with method for alerts page"""

import logging
import time

import allure

from conf.conf import Timeouts
from conf.locators.alerts_frame_windows_locators import AlertsPageLocators
from generator.generator import generate_person
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AlertsPage(BasePage):
    """A class alerts page"""
    locators = AlertsPageLocators()

    @allure.step('Check alerts text')
    def check_alert_text(self):
        logger.info('Click Button')
        self.element_is_visible(self.locators.ALERT_BTN).click()
        return self.go_to_alert().text

    @allure.step('Check alert text appear time')
    def check_alert_appear_time(self):
        logger.info('Click Button')
        self.element_is_visible(self.locators.TIMER_ALERT_BTN).click()
        time.sleep(Timeouts.sec_10)
        return self.go_to_alert().text

    @allure.step('Check confirm alert')
    def check_confirm_alert(self):
        logger.info('Click Button')
        self.element_is_visible(self.locators.CONFIRM_BTN_ALERT).click()
        self.go_to_alert().accept()
        return self.element_is_visible(self.locators.RESULT_CONFIRM_ALERT).text

    @allure.step('Check promt after result')
    def check_promt_alert_result(self):
        person = next(generate_person())
        name = person.first_name
        logger.info('Click Button')
        self.element_is_visible(self.locators.LOGIN_ALERT_BTN).click()
        alert_window = self.go_to_alert()
        alert_window.send_keys(name)
        alert_window.accept()
        confirm_result = self.element_is_visible(self.locators.PROMT_ALERT_RESULT).text.split(' ')
        logger.info(f'Result entered {confirm_result[2]}')
        return name, confirm_result[2]
