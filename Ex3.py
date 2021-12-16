from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

link = "https://stepik.org/lesson/236895/step/1"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    input_1 = browser.find_element_by_css_selector("textarea[spellcheck='false']")
    answer = str(math.log(int(time.time())))
    input_1.send_keys(answer)

    button_1 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))

    # button_1 = browser.find_element_by_class_name("submit-submission")
    button_1.click()

finally:
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()