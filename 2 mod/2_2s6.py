from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(c):
    return str(math.log(abs(12 * math.sin(int(c)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    x = calc(x)

    browser.find_element(By.ID, "answer").send_keys(x)
    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    but = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", but)
    but.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()