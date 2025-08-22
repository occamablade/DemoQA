# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# options = Options()
# # options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# # driver.implicitly_wait(5)
# # driver.maximize_window()
# driver.get('https://demoqa.com/checkbox')
# driver.find_element(By.XPATH, '//button[@title="Expand all"]').click()
# fields = driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
# data = []
#
# for field in fields:
#     data.append(field.text)
#
# print(data)
# sleep(30)
#
# driver.quit()

class CodeStatus:

    codes = {
        'Created': {'code': '201',
                    'text': 'Created'},
        'No Content': {'code': '204',
                       'text': 'No Content'},
        'Moved': {'code': '301',
                  'text': 'Moved Permanently'},
        'Bad Request': {'code': '400',
                        'text': 'Bad Request'},
        'Unauthorized': {'code': '401',
                         'text': 'Unauthorized'},
        'Forbidden': {'code': '403',
                      'text': 'Forbidden'},
        'Not Found': {'code': '404',
                      'text': 'Not Found'},
    }

print(CodeStatus.codes['Created'])