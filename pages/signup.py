from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random


class SignupPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver);

    def click_on_signup(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.dropdown--signup')))
        signup_form = self.driver.find_element_by_css_selector('.dropdown--signup')
        signup_form.click()

    def fill_signup_form(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#id_fullname')))
        name_elem = self.driver.find_element_by_css_selector('#id_fullname')
        name_elem.send_keys("Jhon Don")
        email_elem = self.driver.find_element_by_css_selector('input[id="email--1"]')
        rand_num = str(random.randint(111,999))
        rand_email= "bbaig" + rand_num +"@gmail.com"
        email_elem.send_keys(rand_email)
        password_list=['JhonDon','Chrisitian','Elizabeth']
        rand_pass = random.choice(password_list)+ rand_num
        pass_elem = self.driver.find_element_by_css_selector('#password')
        pass_elem.send_keys(rand_pass)
        submit_form = self.driver.find_element_by_css_selector('#submit-id-submit')
        submit_form.click()
        return rand_email, rand_pass

    def logout_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href*="edit-profile"]')))
        logout_elem = self.driver.find_element_by_css_selector('a[href*="edit-profile"]')
        self.action.move_to_element(logout_elem).perform()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/logout/"]')))
        logout_elem2 = self.driver.find_element_by_css_selector('a[href*="/logout/"]')
        logout_elem2.click()


