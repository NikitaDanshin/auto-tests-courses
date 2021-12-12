from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button_1 = browser.find_element_by_css_selector("button[type = 'submit']")
    button_1.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(y)

    button_2 = browser.find_element_by_css_selector("button.btn")
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()


