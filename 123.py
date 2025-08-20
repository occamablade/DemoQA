from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(5)
# driver.maximize_window()
driver.get('https://demoqa.com/checkbox')
driver.find_element(By.XPATH, '//button[@title="Expand all"]').click()
fields = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
data = []

for field in fields:
    data.append(field.text)

print(data)
sleep(30)

driver.quit()