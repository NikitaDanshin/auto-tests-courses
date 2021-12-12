from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name('first_block .form-control.first')
    input1.send_keys("Kot")
    input2 = browser.find_element_by_class_name('first_block .form-control.second')
    input2.send_keys("Kot")
    input3 = browser.find_element_by_class_name('first_block .form-control.third')
    input3.send_keys("Kot")

    button = browser.find_element_by_xpath('//button[@type = "submit"]')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(1)
finally:
    time.sleep(3)
    browser.quit()

