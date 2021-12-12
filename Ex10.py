from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(y)

    check_1 = browser.find_element_by_id("robotCheckbox")
    check_1.click()


    radio_1 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_1)
    radio_1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()