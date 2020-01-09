from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Next"]')))
        return True

    def click_on_login(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.dropdown--login')))
        login_form = self.driver.find_element_by_css_selector('.dropdown--login')
        login_form.click()

    def fill_login_form(self, email, password):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-item-email [type="email"]')))
        login_email_elem = self.driver.find_element_by_css_selector('#form-item-email [type="email"]')
        login_email_elem.send_keys(email)
        login_pass_elem = self.driver.find_element_by_css_selector('#form-item-password .textinput')
        login_pass_elem.send_keys(password)
        submit_login_form = self.driver.find_element_by_css_selector('#submit-id-submit')
        submit_login_form.click()
