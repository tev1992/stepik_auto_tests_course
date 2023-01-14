import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    # price = "$100"
    text_100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book[onclick='checkPrice();']").click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
    # time.sleep(2)

finally:
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    text_copy = alert_text.split(": ")[-1]
    print(text_copy)
    browser.quit()