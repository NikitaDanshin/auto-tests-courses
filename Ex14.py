from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button_book = browser.find_element_by_id("book")
    button_book.click()

    input_1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_1)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_1.send_keys(y)

    button_submit = browser.find_element_by_id("solve")
    button_submit.click()



finally:
    time.sleep(10)
    browser.quit()


