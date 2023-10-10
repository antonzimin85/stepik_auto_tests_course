from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(c):
    return str(math.log(abs(12 * math.sin(int(c)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.TAG_NAME, 'img')
    val = x.get_attribute("valuex")
    val = calc(val)
    browser.find_element(By.ID, "answer").send_keys(val)
    time.sleep(2)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    time.sleep(2)
    radio = browser.find_element(By.ID,'robotsRule')
    radio.click()
    time.sleep(2)
    but = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    but.click()


finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()