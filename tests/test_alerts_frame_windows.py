"""Module with test for alerts, frame and windows page"""

import allure

from conf.locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators, FramePageLocators, \
    NestedFramePageLocators, ModalDialogPageLocators
from pages.alerts_frame_windows.alerts import AlertsPage
from pages.alerts_frame_windows.browser_windows import AlertsFrameWindowsPage
from pages.alerts_frame_windows.frames import FramesPage
from pages.alerts_frame_windows.modal_dialogs import ModalDialogsPage
from pages.alerts_frame_windows.nested_frames import NestedFramesPage


@allure.suite('Alerts, frame and windows page')
class TestAlertsFrameWindowsPage:

    @allure.epic('Browser Windows page')
    class TestBrowserWindowsPage:

        @allure.feature('Test New Tab')
        def test_new_tab(self, driver):
            browser_windows = AlertsFrameWindowsPage(driver, BrowserWindowsLocators.BROWSER_WINDOWS_LINK)
            browser_windows.open()
            assert browser_windows.new_tab_page() == 'This is a sample page', 'Wrong text on the page'

        @allure.feature('Test New Window')
        def test_new_window(self, driver):
            browser_windows = AlertsFrameWindowsPage(driver, BrowserWindowsLocators.BROWSER_WINDOWS_LINK)
            browser_windows.open()
            assert browser_windows.new_window_page() == 'This is a sample page', 'Wrong text on the page'

    @allure.epic('Alerts page')
    class TestAlertsPage:

        @allure.feature('Check alert text')
        def test_alert_text(self, driver):
            alerts_page = AlertsPage(driver, AlertsPageLocators.ALERTS_LINK)
            alerts_page.open()
            alert_text = alerts_page.check_alert_text()
            assert alert_text == 'You clicked a button', 'Alert is not present'

        @allure.feature('Check alert appear 5 sec')
        def test_alert_appear_time(self, driver):
            alerts_page = AlertsPage(driver, AlertsPageLocators.ALERTS_LINK)
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_time()
            assert alert_text == 'This alert appeared after 5 seconds', 'You do not press OK on the ' \
                                                                        'alert window after 5 second'

        @allure.feature('Check confirm alert')
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, AlertsPageLocators.ALERTS_LINK)
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'You do not press OK on the alert window'

        @allure.feature('Check promt alert result')
        def test_promt_alert_result(self, driver):
            alerts_page = AlertsPage(driver, AlertsPageLocators.ALERTS_LINK)
            alerts_page.open()
            send_text, result_text = alerts_page.check_promt_alert_result()
            assert send_text == result_text, 'The entered text in the alert ' \
                                             'window does not match the result'

    @allure.epic('Frames page')
    class TestFramesPage:

        @allure.step('Check frame size')
        def test_frame_size(self, driver):
            frame_page = FramesPage(driver, FramePageLocators.FRAME_LINK)
            frame_page.open()
            big_frame_size = frame_page.check_big_frmae()
            small_frame_size = frame_page.check_small_frame()
            assert big_frame_size == ['This is a sample page', '500px', '350px'], 'The frame 1 does not exist'
            assert small_frame_size == ['This is a sample page', '100px', '100px'], 'The frame 2 does not exist'


    @allure.epic('Test Nested Frames Page')
    class TestNestedFramesPage:

        @allure.feature('Check nested frame')
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramesPage(driver, NestedFramePageLocators.NESTED_FRAME_LINK)
            nested_frame_page.open()
            parent_frame, child_frame = nested_frame_page.check_nested_frame()
            assert parent_frame == 'Parent frame', 'Parent frame has not been present'
            assert child_frame == 'Child Iframe', 'Child frame has not been present'

    @allure.epic('Test Modal Dialog Page')
    class TestModalDialogPage:

        @allure.feature('Check small modal window')
        def test_small_modal_window(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, ModalDialogPageLocators.MODAL_DIALOG_LINK)
            modal_dialog_page.open()
            modal_title, modal_text = modal_dialog_page.check_small_modal_window()
            assert modal_title == 'Small Modal', 'Invalid title text'
            assert modal_text == 'This is a small modal. It has very less content', 'Invalid modal window text'

        @allure.feature('Check large modal window')
        def test_large_modal_window(self, driver):
            modal_dialog_page = ModalDialogsPage(driver,  ModalDialogPageLocators.MODAL_DIALOG_LINK)
            modal_dialog_page.open()
            modal_title, modal_text = modal_dialog_page.check_large_modal_window()
            assert modal_title == 'Large Modal', 'Invalid title text'
            assert modal_text == 574, 'Incorrect text length'
