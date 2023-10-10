from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAbs(unittest.TestCase):

    def test_text(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .form-control.second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block > div > .form-control.third')
        input3.send_keys("test@test.test")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'Should be another text')

        browser.quit()

if __name__ == "__main__":
    unittest.main()