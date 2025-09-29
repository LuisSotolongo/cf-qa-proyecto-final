import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

class SignupPage(BasePage):

    URL = f"{SHOPHUB_BASE_URL}/signup"

    def __init__(self, driver):
        self.driver = driver
        self.signup_button_page = (By.XPATH, "//a[@href='/signup']")
        self.firstName_input = (By.ID, "firstName")
        self.lastName_input = (By.ID, "lastName")
        self.email_input = (By.ID, "email")
        self.zipCode_input = (By.ID, "zipCode")
        self.password_input = (By.ID, "password")
        self.signup_button = (By.XPATH, "//button[@type='submit']")


    def load(self):
        self.driver.get(self.URL)


    def signup(self, first_name,last_name, email, zip_code, password):
        WebDriverWait(self.driver, 100 ).until(EC.presence_of_element_located(self.firstName_input))
        self.driver.find_element(*self.firstName_input).clear()
        self.driver.find_element(*self.firstName_input).send_keys(first_name)
        self.driver.find_element(*self.lastName_input).clear()
        self.driver.find_element(*self.lastName_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.zipCode_input).clear()
        self.driver.find_element(*self.zipCode_input).send_keys(zip_code)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signup_button).click()