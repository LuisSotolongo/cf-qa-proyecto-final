import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

load_dotenv()
SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")

class LoginPage(BasePage):

    URL = f"{SHOPHUB_BASE_URL}/login"

    def __init__(self, driver):
        self.driver = driver
        self.login_button_page = (By.XPATH, "//a[@href='/login']")
        self.username_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")


    def load(self):
        self.driver.get(self.URL)


    def login(self, username, password):
        WebDriverWait(self.driver, 100 ).until(EC.presence_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


