import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        try:
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
            enter_message = "Congratulations! You have successfully registered!"
            self.assertEqual(enter_message, welcome_text,
                             "Strings should be equals")
        finally:
            time.sleep(3)
            browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        try:
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
            enter_message = "Congratulations! You have successfully registered!"
            self.assertEqual(enter_message, welcome_text,
                             "Strings should be equals")
            time.sleep(1)
        finally:
            time.sleep(3)
            browser.quit()

if __name__ == "__main__":
    unittest.main()