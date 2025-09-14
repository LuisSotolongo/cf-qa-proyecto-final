import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException

SHOPHUB_BASE_URL = os.getenv("SHOPHUB_BASE_URL")


class CheckoutPage(BasePage):

    URL = f"{SHOPHUB_BASE_URL}"
    CHECKOUT_URL = f"{SHOPHUB_BASE_URL}/checkout"

    def __init__(self, driver):
        self.driver = driver
        self.firstName_input = (By.ID, "firstName")
        self.lastName_input = (By.ID, "lastName")
        self.email_input = (By.ID, "email")
        self.phone_input = (By.ID, "phone")
        self.address_input = (By.ID, "address")
        self.city_input = (By.XPATH, "//input[@id='city']")
        self.zipCode_input = (By.XPATH, "//input[@id='zipCode']")
        self.country_input = (By.XPATH, "//input[@id='country']")
        self.place_order_button = (By.ID, "place-order-button")
        self.order_summary_text = (By.XPATH, "//div[@id='order-summary-title' and text()='Order Summary']")
        self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
        self.resume_page_text = (By.XPATH, "//h1[text()='No Order Found']")


    def load(self):
        self.driver.get(self.URL)

    def open_checkout_page(self):
        self.driver.get(self.CHECKOUT_URL)

    def fill_checkout_form(self, first_name, last_name, email, phone, address, city, zip_code, country):
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.firstName_input))
            self.driver.find_element(*self.firstName_input).clear()
            self.driver.find_element(*self.firstName_input).send_keys(first_name)
            self.driver.find_element(*self.lastName_input).clear()
            self.driver.find_element(*self.lastName_input).send_keys(last_name)
            self.driver.find_element(*self.email_input).clear()
            self.driver.find_element(*self.email_input).send_keys(email)
            self.driver.find_element(*self.phone_input).clear()
            self.driver.find_element(*self.phone_input).send_keys(phone)
            self.driver.find_element(*self.address_input).clear()
            self.driver.find_element(*self.address_input).send_keys(address)
            self.driver.find_element(*self.city_input).clear()
            self.driver.find_element(*self.city_input).send_keys(city)
            self.driver.find_element(*self.zipCode_input).clear()
            self.driver.find_element(*self.zipCode_input).send_keys(zip_code)
            self.driver.find_element(*self.country_input).clear()
            self.driver.find_element(*self.country_input).send_keys(country)
            time.sleep(30)

    def checkout_is_not_empty(self):
        try:
            self.wait_for_invisibility_of_element(self.loader)
            self.wait_until_visible(self.order_summary_text)
            order_summary = self.text_of_element(self.order_summary_text)
            print(order_summary)
        except TimeoutException:
            raise AssertionError("El resumen del pedido no se encontró en la página de pago.")


    def checkout_resume_order(self):
        try:
            self.wait_for_invisibility_of_element(self.loader)
            self.wait_until_visible(self.resume_page_text)
            resume_text = self.text_of_element(self.resume_page_text)

        except TimeoutException:
            raise AssertionError("El mensaje de reanudación del pedido no se encontró en la página de pago.")


    def place_order(self):
        self.click(self.place_order_button)
        self.wait_for_invisibility_of_element(self.loader)