from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    z = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()