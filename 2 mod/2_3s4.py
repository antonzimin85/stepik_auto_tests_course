from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(c):
    return str(math.log(abs(12 * math.sin(int(c)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    bt = browser.find_element(By.CSS_SELECTOR, 'button')
    bt.click()

    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    x = calc(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    but = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    but.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()