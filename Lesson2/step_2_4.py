from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/wait1.html"
# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get(link)
#
# button = browser.find_element(By.CSS_SELECTOR, "#verify").click()
# message = browser.find_element(By.CSS_SELECTOR, "#verify_message").text
# assert "successful" in message, f"текст не соответствует - {message}"
# browser.quit()

link2 = "http://suninjuly.github.io/cats.html"
browser2 = webdriver.Chrome()
browser2.get(link2)

browser2.find_element(By.ID, "button").click()
browser2.quit()
