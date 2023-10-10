from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '2_8.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    fn.send_keys('Anton')
    ln = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    ln.send_keys('Ivamov')
    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    email.send_keys('test@test.test')
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)
    but = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    but.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()