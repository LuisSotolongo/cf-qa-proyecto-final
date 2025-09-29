import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shophub_ui_test.pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException


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
        self.city_input = (By.ID, "city")
        self.zipCode_input = (By.ID, "zipCode")
        self.country_input = (By.ID, "country")
        self.place_order_button = (By.ID, "place-order-button")
        self.order_summary_text = (By.XPATH, "//div[@id='order-summary-title' and text()='Order Summary']")
        self.loader = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
        self.resume_page_text = (By.XPATH, "//h1[text()='No Order Found']")
        self.confirmation_page_text = (By.XPATH, "//h1[contains(@class, 'text-3xl') and contains(@class, 'font-bold') and contains(text(), 'No Order Found')]")

    def load(self):
        self.driver.get(self.URL)

    def open_checkout_page(self):
        self.driver.get(self.CHECKOUT_URL)

    def fill_checkout_form(self, first_name="luis", last_name="rodriguez", email="luis@mail.com", phone=999222233, address="bla bla", city="bla bla", zip_code=44556, country="Spain"):
        try:
            self.wait_for_element(self.firstName_input)
            self.type(self.firstName_input, first_name)
            self.type(self.lastName_input, last_name)
            self.type(self.email_input, email)
            self.type(self.phone_input, phone)
            self.type(self.address_input, address)
            self.type(self.city_input, city)
            self.type(self.zipCode_input, zip_code)
            self.type(self.country_input, country)
            time.sleep(2)
        except UnexpectedAlertPresentException:
            self.handle_alert("Please fill in all required fields")

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


    def click_place_order_button(self):
        try:
            self.wait_for_invisibility_of_element(self.loader)
            self.wait_for_element(self.place_order_button)
            self.click(self.place_order_button)
        except UnexpectedAlertPresentException:
            self.handle_alert("Please fill in all required fields")
        except TimeoutException:
            try:
                self.handle_alert("Please fill in all required fields")
            except AssertionError:
                raise AssertionError("No se encontró el botón de realizar pedido ni el alert esperado.")

    def handle_alert(self, expected_text):
        try:
            self.wait_for_alert()
            alert = self.driver.switch_to.alert
            assert alert.text == expected_text, f"Texto de alerta incorrecto. Esperado: '{expected_text}', Obtenido: '{alert.text}'"
            alert.accept()
        except TimeoutException:
            raise AssertionError("No se encontró ninguna alerta.")
        except UnexpectedAlertPresentException:
            raise AssertionError("Se encontró una alerta inesperada.")

        def get_confirmation_header_text(self):
            return self.text_of_element(self.confirmation_page_text)