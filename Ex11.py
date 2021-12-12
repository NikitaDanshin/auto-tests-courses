from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    input_1 = browser.find_element_by_css_selector("input[name = 'firstname']")
    input_1.send_keys("Cat")
    input_2 = browser.find_element_by_css_selector("input[name = 'lastname']")
    input_2.send_keys("Cat")
    input_2 = browser.find_element_by_css_selector("input[name = 'email']")
    input_2.send_keys("Cat")

    current_dir = os.path.abspath(os.path.dirname("C:/files/"))
    file_path = os.path.join(current_dir, "ex.txt")
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()