from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    image_1 = browser.find_element_by_id("treasure")
    x_element = image_1.get_attribute("valuex")

    y = calc(x_element)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(y)

    check_1 = browser.find_element_by_id("robotCheckbox")
    check_1.click()

    radio_1 = browser.find_element_by_css_selector("[value = 'robots']")
    radio_1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()