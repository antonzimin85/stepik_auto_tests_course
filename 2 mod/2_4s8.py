from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import formula


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    btn = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    btn.click()
    x = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x = x.text
    x = formula.calc(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    but = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    but.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()