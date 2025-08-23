"""Module with method for upload and download page"""

import base64
import logging
import os
import random

import allure
from selenium.webdriver.common.by import By

from conf.locators.elements_page_locators import UploadDownloadLocators
from generator.generator import generate_file
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class UploadDownloadPage(BasePage):
    """A class to upload and download page"""

    @allure.step('Upload file')
    def upload_file(self):
        file_name, path = generate_file()
        self.driver.find_element(By.XPATH, UploadDownloadLocators.UPLOAD_BTN).send_keys(path)
        file = file_name.split('\\')[-1]
        logger.info(f'File uploaded: {file}')
        name_uploaded_file = self.driver.find_element(By.XPATH, UploadDownloadLocators.RESULT_UPLOADED_BTN).text
        name_uploaded_file = name_uploaded_file.split('\\')[-1]
        logger.info(f'Remove {file}')
        os.remove(path)
        return file, name_uploaded_file

    @allure.step('Download file')
    def download_file(self):
        link = self.driver.find_element(By.XPATH, UploadDownloadLocators.DOWNLOAD_BTN).get_attribute('href')
        logger.info(f'Get encoded link href: {link}')
        link_b = base64.b64decode(link)
        logger.info('Decode the link into bytes')
        path_name_file = rf'C:\Users\vanyshqa\Desktop\jib\DemoQA\FileTestjpg{random.randint(0, 999)}.jpg'
        file_name = path_name_file.split('\\')[-1]
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            logger.info('We cut off unnecessary values from the decoded code to the desired one')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            logger.info(f'Checking that the downloaded file <{file_name}> in the {path_name_file}')
            f.close()
        os.remove(path_name_file)
        logger.info(f'Remove {file_name}')
        return check_file
