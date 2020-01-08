import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login import LoginPage
from pages.home import HomePage
from pages.signup import SignupPage


class Udemy(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Firefox()
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.signup = SignupPage(self.driver)

    def test_login(self):
        self.driver.get('https://www.udemy.com/')
        self.assertTrue(self.home.is_browser_on_the_page())
        self.signup.click_on_signup()
        email, passw = self.signup.fill_signup_form()
        self.signup.logout_page()
        self.driver.delete_all_cookies()
        self.login.click_on_login()
        self.login.fill_login_form(email, passw)
        # self.assertTrue(self.login.is_browser_on_the_page())

if __name__ == '__main__':
    unittest.main()
