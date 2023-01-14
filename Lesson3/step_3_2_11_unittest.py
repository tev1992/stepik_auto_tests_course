# unittwst
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def elements(link):
    browser = webdriver.Chrome()
    browser.get(link)
    First_name = browser.find_element(By.CSS_SELECTOR, ".first[required]").send_keys("Имя")
    Last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]").send_keys("Фамилия")
    Email = browser.find_element(By.CSS_SELECTOR, ".third[required]").send_keys("Email")

    button = browser.find_element(By.CSS_SELECTOR, "[type*='submit']").click()
    proverka = browser.find_element(By.CSS_SELECTOR, "h1").text

    return proverka

class TestLink(unittest.TestCase):

    def test_link1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(elements(link1), "Congratulations! You have successfully registered!")

    def test_link2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(elements(link2), "Congratulations! You have successfully registered!")

if __name__ == '__main__':
    unittest.main()