from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
import time

class KayakFrontDoor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://www.kayak.com/flights')
        time.sleep(5)

    def test_1_title(self):
        header_title = self.driver.title
        self.assertEqual(header_title, "Cheap Flights, Airline Tickets & Airfare Deals | KAYAK")
        time.sleep(5)

    def test_2_login(self):
        signin_elem = self.driver.find_element_by_css_selector(".js-trigger-label div:first-child")
        signin_elem.click()
        time.sleep(3)
        email_elem = self.driver.find_element_by_css_selector('[id$="loginContainer"] [aria-label="Email Address"]')
        email_elem.send_keys("testkyk@yandex.com")
        pass_elem = self.driver.find_element_by_css_selector('[id$="loginContainer"] [aria-label="Password"]')
        pass_elem.send_keys("*********")
        remember_elem = self.driver.find_element_by_css_selector('[id$="loginContainer"] [type="checkbox"]')
        remember_elem.click()
        submit_elem = self.driver.find_element_by_css_selector('[id$="loginContainer"] [aria-label="Sign in"]')
        submit_elem.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()





if __name__ == '__main__':
    unittest.main()
