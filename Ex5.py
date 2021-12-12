from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_class_name("first_block .form-control")
    for element in elements:
        element.send_keys("Кот")

    button = browser.find_element_by_xpath('//button[@type = "submit"]')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(2)
finally:
    time.sleep(30)
    browser.quit()

