from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f_dig = browser.find_element(By.ID, 'num1')
    f_dig = f_dig.text
    s_dig = browser.find_element(By.ID, 'num2')
    s_dig = s_dig.text
    summ = int(f_dig) + int(s_dig)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))
    but = browser.find_element(By.CSS_SELECTOR,'[type="submit"]')
    but.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()